# -*- coding: utf-8 -*-
# Display LCD + LDR. Pier Calderan 2015.
#!/usr/bin/python
import RPi.GPIO as GPIO, time, os
from Adafruit_CharLCD import Adafruit_CharLCD
GPIO.setmode(GPIO.BCM)

lcd = Adafruit_CharLCD()
lcd.begin(16,1)
     
def RC_time (PinRC):
      counter = 0
      GPIO.setup(PinRC, GPIO.OUT)
      GPIO.output(PinRC, GPIO.LOW)
      time.sleep(0.1)
      GPIO.setup(PinRC, GPIO.IN)
      while (GPIO.input(PinRC) == GPIO.LOW):
            counter += 1
      return counter
     
while True:
      lcd.clear()
      ldr= RC_time(21)
# manda al display la lettura del valore LDR
      lcd.message('LDR %s' % ( ldr ) )
# ritardo di un secondo
      time.sleep(1) 
