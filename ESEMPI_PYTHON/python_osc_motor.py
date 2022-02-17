# USARE PYTHON 2.7
# Test PWM motori DC con integrato L293 e controllo OSC
# Pier Calderan 2015
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import OSC, threading
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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

receive_address = '169.254.129.131', 8000

s = OSC.OSCServer(receive_address) 
s.addDefaultHandlers()
def printing_handler(addr, tags, stuff, source):
    dati=int(stuff[0])
    
    if (addr=="/1/fader1"):
        if (dati > 0):
            motor1.avanti(dati)
        if (dati < 0):
            motor1.indietro(abs(dati))
            
    if (addr=="/1/fader2"):        
        if (dati > 0):
            motor2.avanti(dati)
        if (dati < 0):
            motor2.indietro(abs(dati))

s.addMsgHandler("/1/fader1", printing_handler)
s.addMsgHandler("/1/fader2", printing_handler)

print "Handler :"
for addr in s.getOSCAddressSpace():
    print addr
print "\nAvvio del server OSC. Usare Ctrl-C per terminare."
st = threading.Thread( target = s.serve_forever )
st.start()    

try :
    while 1 :
        sleep(0.2)

except KeyboardInterrupt :
    print "\nChiusura del server OSC..."
    s.close()
    print "In attesa della chiusura del server"
    st.join() 
    print "Fatto!"
    GPIO.cleanup()
    


