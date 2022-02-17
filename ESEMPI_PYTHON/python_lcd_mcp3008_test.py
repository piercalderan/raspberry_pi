# Visualizzazione su LCD di un potenziometro di volume
# 2015 Pier Calderan
# -*- coding: utf-8 -*-
# Importazione delle librerie GPIO e time
import time
import os
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD()
lcd.begin(16,1)

GPIO.setmode(GPIO.BCM)
# Funzione di lettura dei dati SPI di otto ingressi MCP3008
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
            if ((adcnum > 7) or (adcnum < 0)):
                    return -1
            GPIO.output(cspin, True)
            GPIO.output(clockpin, False)  # Imposta il clock low
            GPIO.output(cspin, False)     # Imposta CS low 
     
            commandout = adcnum
            commandout |= 0x18  # Start bit + single-ended bit
            commandout <<= 3    # Sono necessari solo 5 bit con uno shift di 3 bit
            for i in range(5):
                    if (commandout & 0x80):
                            GPIO.output(mosipin, True)
                    else:
                            GPIO.output(mosipin, False)
                    commandout <<= 1
                    GPIO.output(clockpin, True)
                    GPIO.output(clockpin, False)
     
            adcout = 0
            for i in range(12):
                    GPIO.output(clockpin, True)
                    GPIO.output(clockpin, False)
                    adcout <<= 1
                    if (GPIO.input(misopin)):
                            adcout |= 0x1
     
            GPIO.output(cspin, True)
            
            adcout >>= 1       # Il primo bit è null e viene ignorato
            return adcout
     
# Si possono assegnare i pin SPI a piacere oppure lasciare quelli di default
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
     
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
     
# Lettura del potenziometro dalla porta SPI
potentiometer_adc = 0
     
last_read = 0       # Variabile per conservare l'ultimo valore del potenziometro
tolerance = 5       # Tolleranza per evitare bruschi cambiamenti di volume
                    
     
while True:
            # Variabile che memorizza lo stato del potenziometro
            trim_pot_changed = False
     
            # Lettura del potenziometro dalla porta SPI
            trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
                        
 # Questa variabile fa la differenza dall'ultima lettura e quella attuale e arrotonda
 # al valore assoluto per stampare solo il valore di quando si cambia il volume
 
            pot_adjust = abs(trim_pot - last_read)
     
            if ( pot_adjust > tolerance ):
                   trim_pot_changed = True
     
            if ( trim_pot_changed ):
                    set_volume = trim_pot / 10.24           
                    set_volume = round(set_volume)          # Arrotondamento ai valori interi
                    set_volume = int(set_volume)            # Rende intero il valore del volume
# Stampa il valore in percentuale
# e manda il valore del volume all'uscita audio del mixer
                    print ('Volume = {volume}%' .format(volume = set_volume))
                    lcd.clear()
                    
                    lcd.message("Volume audio\n")
                    
                    lcd.message(str(set_volume))
                    set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = set_volume)
                    os.system(set_vol_cmd)  # Imposta il volume di sistema
     
                    # Salva la lettura del potenziometro per il prossimo ciclo
                    last_read = trim_pot
     
            # Ritardo di 0,1 secondi per un intervento soft
            time.sleep(0.1)
