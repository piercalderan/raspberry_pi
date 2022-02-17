# Visualizzazione su LCD di un luxmetro
# 2015 Pier Calderan.
# -*- coding: utf-8 -*-
import time
import os

from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD()
lcd.begin(16,1)

from setgpio import readadc

SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

lux_adc = 1
     
r_pulldown = 10000.0
v_in = 3.3
ldr_1 = 70000.0
gamma = -0.7

while True:
    val_ldr = readadc(lux_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    v_out = v_in / 1024 * val_ldr
    if (v_out > 0):
        ldr = r_pulldown * v_in/v_out - r_pulldown
        lux = pow((ldr/ldr_1),(1.0/gamma))
        lux = "{0:.2f}".format(lux)
        lcd.clear()
        lcd.message("Lux\n")
        lcd.message(str(lux))
        time.sleep(0.5)
