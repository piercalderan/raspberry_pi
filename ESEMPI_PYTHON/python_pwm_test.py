# Test di un motore servo tramite PWM
# Pier Calderan 2015
# -*- coding: utf-8 -*-
# Importazione delle librerie GPIO, sys e time
import RPi.GPIO as GPIO, time, sys


# Impostazione del pin GPIO7 di uscita PWM
PWM_pin = 26

# Ritardo fra le posizioni del servomotore
delay_time = 0.02 # Impostazione del ritardo predefinito
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_pin, GPIO.OUT)
GPIO.output(PWM_pin, True)

while True:
    try:
### PWM di 1 ms
        for i in range(1, 1000):
            GPIO.output(PWM_pin, False)
            time.sleep(0.001)
            GPIO.output(PWM_pin, True)
            time.sleep(0.001) # Ritardo predefinito

# PWM di 1,5 ms
        for i in range(1, 1000):
            GPIO.output(PWM_pin, False)
            time.sleep(0.0015)
            GPIO.output(PWM_pin, True)
            time.sleep(0.0015) # Ritardo predefinito
##
### PWM di 2 ms
        for i in range(1, 1000):
            GPIO.output(PWM_pin, False)
            time.sleep(0.002)
            GPIO.output(PWM_pin, True)
            time.sleep(0.002) # Ritardo predefinito
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
