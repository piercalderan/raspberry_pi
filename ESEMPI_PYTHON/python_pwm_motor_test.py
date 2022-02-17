# Test accelerazione PWM motori DC con integrato L293. Pier Calderan 2015
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)

class Motor: # Classe per inizializzare il motore con i tre controlli e avvia la PWM
    def __init__(self, pin_1A, pin_2A, pin_EN):        
        self.pin_1A = pin_1A
        self.pin_2A = pin_2A
        self.pin_EN = pin_EN
        GPIO.setup(self.pin_1A, GPIO.OUT)
        GPIO.setup(self.pin_2A, GPIO.OUT)
        GPIO.setup(self.pin_EN, GPIO.OUT)
        self.pwm_avanti = GPIO.PWM(self.pin_1A, 100)
        self.pwm_indietro = GPIO.PWM(self.pin_2A, 100)
        self.pwm_avanti.start(0)
        self.pwm_indietro.start(0)
        GPIO.output(self.pin_EN,GPIO.HIGH) 

    def avanti(self, speed): # Funzione avanti        
        self.pwm_indietro.ChangeDutyCycle(0)
        self.pwm_avanti.ChangeDutyCycle(speed)    

    def indietro(self, speed): # Funzione indietro        
        self.pwm_avanti.ChangeDutyCycle(0)
        self.pwm_indietro.ChangeDutyCycle(speed)

    def stop(self): # Funzione stop
        self.pwm_avanti.ChangeDutyCycle(0)
        self.pwm_indietro.ChangeDutyCycle(0)

motor1 = Motor(17, 4, 18) # istanza del motore 1
motor2 = Motor(24, 9, 8)  # istanza del motore 2

print ("Test accelerazione")
for vel in range (20,100):
    motor1.avanti(vel)
    motor2.indietro(vel)
    sleep(0.2)
motor1.stop()
motor2.stop()

for vel in range (20,100):
    motor1.indietro(vel)
    motor2.avanti(vel)
    sleep(0.2)
motor1.stop()
motor2.stop()

print ("Test 1")
motor1.avanti(50)
motor2.indietro(70)
sleep(4)

print ("Test 2")
motor1.indietro(70)
motor2.avanti(50)
sleep(4)

print ("Test 3")
motor1.avanti(30)
motor2.avanti(30)
sleep(4)

print ("Test 4")
motor1.indietro(100)
motor2.indietro(100)
sleep(4)

print ("STOP")
motor1.stop()
motor2.stop()
GPIO.cleanup()
