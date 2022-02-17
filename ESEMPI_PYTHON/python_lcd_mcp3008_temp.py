# Visualizzazione su LCD di un potenziometro e di un sensore di temperatura
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
temperature_adc = 1
     
last_read = 0       # Variabile per conservare l'ultimo valore del potenziometro
tolerance = 5       # Tolleranza per evitare bruschi cambiamenti di volume
     
while True:
            # Variabile che memorizza lo stato del potenziometro
            trim_pot_changed = False
     
            # Lettura del potenziometro dalla porta SPI canale 0
            trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
            # Lettura del sensore di temperatrura dalla porta SPI canale 1
            temp = readadc(temperature_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
            step = 3.3 / 1024 # tensione per ogni livello
            set_temp = temp * step / 0.01 # conversione in gradi C
            set_fahr = int(set_temp * 1.8 + 32) # conversione in fahrenheit
            set_temp = "{0:.2f}".format(set_temp)
            
            pot_adjust = abs(trim_pot - last_read)
     
            if ( pot_adjust > tolerance ):
                   trim_pot_changed = True
     
            if ( trim_pot_changed ):
                    set_volume = trim_pot / 10.24           # convert 10bit adc0 (0-1024) trim pot read into 0-100 volume level
                    set_volume = round(set_volume)          # round out decimal value
                    set_volume = int(set_volume)            # cast volume as integer
     
                    print ('Volume = {volume}%' .format(volume = set_volume))
                    lcd.clear()
                    
                    lcd.message("Vol. Temperatura\n")
                    
                    lcd.message(str(set_volume))
                    lcd.message("   " + str(set_temp) + " " + str(set_fahr))
                    set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = set_volume)
                    os.system(set_vol_cmd)  # set volume
     
                    # save the potentiometer reading for the next loop
                    last_read = trim_pot
     
            # hang out and do nothing for a half second
            time.sleep(0.1)
