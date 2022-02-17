# Test motori DC con integrato L293. Pier Calderan 2015.
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)

Motor1A = 26 #1A
Motor2A = 4  #2A
Motor1E = 18 #1,2EN

Motor3A = 24 #3A
Motor4A = 9  #4A
Motor3E = 8  #3,4EN
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor3E,GPIO.OUT)
 
print ("AVANTI")
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor3A,GPIO.LOW)
GPIO.output(Motor4A,GPIO.HIGH)
GPIO.output(Motor3E,GPIO.HIGH)
 
sleep(4)
 
print ("INDIETRO")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
GPIO.output(Motor3A,GPIO.HIGH)
GPIO.output(Motor4A,GPIO.LOW)
GPIO.output(Motor3E,GPIO.HIGH)

sleep(4)
 
print ("STOP")
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor3E,GPIO.LOW)
 
GPIO.cleanup()
