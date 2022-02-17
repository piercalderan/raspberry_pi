# Pyhon Blink. Pier Calderan 2015
# Cambiare il parametro time
# per impostare la temporizzazione
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setwarnings(False)

while True:
        GPIO.output(7, True)
        time.sleep(1)
        GPIO.output(7, False)
        time.sleep(1)
#EOF
