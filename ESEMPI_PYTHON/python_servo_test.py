# Test di un servomotore
# Pier Calderan 2015
# -*- coding: utf-8 -*-
# Importazione delle librerie GPIO e time
import RPi.GPIO as GPIO, time, sys
# Impostazione del pin GPIO26 di uscita PWM
PWM_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_pin, GPIO.OUT)

hertz=50 # frequenza PWM
pwm = GPIO.PWM(PWM_pin, hertz) # imposta la frequenza PWM
sinistra=0.5 #posizione sinistra
destra=2 #posizione destra
centro=(sinistra+destra)/2 #posizione centrale

poslist=[sinistra,centro,destra,centro] #lista posizioni
ms=1000/hertz #millisecondi

for i in range (5): #loop di 5
    for position in poslist:
        dutycycle = position * 100 / ms #dutycycle in millisecondi
        print("Position: " + str(position))
        pwm.start(dutycycle) #avvia la posizione del servo
        time.sleep(1) #ritardo fra le posizioni
    print("Loop: " + str(i+1)) #stampa il numero del loop
    
pwm.stop #ferma il servo
GPIO.cleanup() #pulisce la porta GPIO
