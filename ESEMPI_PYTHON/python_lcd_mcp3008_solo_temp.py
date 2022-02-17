# Visualizzazione su LCD della temperatura in gradi centigradi e fahrenheit
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
     
# Lettura del sensore di temperatura dalla porta SPI
temperature_adc = 1 # canale 1
     
while True:
            
            # Lettura del sensore di temperaturta dalla porta SPI canale 1
            temp = readadc(temperature_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
            step = 3.3 / 1024 # tensione per ogni livello
            set_temp = temp * step / 0.01 # conversione in gradi C
            set_fahr = set_temp * 1.8 + 32 # conversione in fahrenheit
            set_temp = "{0:.2f}".format(set_temp)
            set_fahr = "{0:.2f}".format(set_fahr)
            
            lcd.clear()
     
            lcd.message("Temperatura\n")
            lcd.message("C:" + str(set_temp) + " F:" + str(set_fahr))
            time.sleep(0.25) # lettura della temperatura ogni 250 ms
