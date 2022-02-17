# Python Button LED On/Off. Pier Calderan 2015
# Premere il pulsante per accendere/spegnere un LED
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
GPIO.output(7, False)

    
while True:
        input_value=GPIO.input(12)
        if input_value == False:
            GPIO.output(7, False)
            print ('Pulsante non premuto. LED spento.')
            time.sleep(0.2)
        elif input_value == True:
            GPIO.output(7, True)
            print ('Pulsante premuto. LED acceso.')
            time.sleep(0.2)
