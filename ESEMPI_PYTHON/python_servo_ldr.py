# Controllo di un servomotore tramite LDR
# Pier Calderan 2015
# -*- coding: utf-8 -*-
# Importazione delle librerie GPIO, sys, time e Adafruit_CharLCD
import time
import sys
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD()
lcd.begin(16,1)

GPIO.setmode(GPIO.BCM)
PWM_pin = 26
GPIO.setup(PWM_pin, GPIO.OUT)
pwm = GPIO.PWM(PWM_pin, 50)

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
            if ((adcnum > 7) or (adcnum < 0)):
                    return -1
            GPIO.output(cspin, True)
     
            GPIO.output(clockpin, False)  
            GPIO.output(cspin, False)     
     
            commandout = adcnum
            commandout |= 0x18  
            commandout <<= 3    
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
            
            adcout >>= 1       
            return adcout
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
     
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
     
lux_adc = 1
     
r_pulldown = 10000.0
v_in = 3.3
ldr_1 = 70000.0
gamma = -0.7
pwm.start(5)
while True:
    try:
        val_ldr = readadc(lux_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        dutycycle =  val_ldr/100 #dutycycle in millisecondi
        print("Position: " + str(dutycycle))
        pwm.ChangeDutyCycle(dutycycle) #avvia la posizione del servo
            
        v_out = v_in / 1024 * val_ldr
        if (v_out > 0):
            ldr = r_pulldown * v_in/v_out - r_pulldown
            lux = pow((ldr/ldr_1),(1.0/gamma))
            lux = "{0:.2f}".format(lux)
            lcd.clear()
            lcd.message("Lux\n")
            lcd.message(str(lux))
            time.sleep(0.5)
    except KeyboardInterrupt:
        sys.exit(0)
        pwm.stop
        GPIO.cleanup()
        
