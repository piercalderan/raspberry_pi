# Esempio di ricezione OSC. Pier Calderan 2015
# -*- coding: utf-8 -*-

import OSC
import time, threading
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(8, 50)
GPIO.output(7, True)
time.sleep(1)
GPIO.output(7, False)
time.sleep(1)
GPIO.output(7, True)
time.sleep(1)
GPIO.output(7, False)
time.sleep(1)
GPIO.output(7, True)
time.sleep(1)


receive_address = '192.168.1.135', 8000

s = OSC.OSCServer(receive_address) 
s.addDefaultHandlers()
def printing_handler(addr, tags, stuff, source):
    dati=int(stuff[0])
    if (stuff==[1.0]):
        GPIO.output(7, True)
    if (stuff==[0.0]):
        GPIO.output(7, False)
    if (addr=="/1/fader1"):
        p.start(0)
        p.ChangeDutyCycle(dati)

s.addMsgHandler("/1/toggle1", printing_handler) 
s.addMsgHandler("/1/fader1", printing_handler) 

print "are :"
for addr in s.getOSCAddressSpace():
    print addr

print "\nAvvio del server OSC. Usare Ctrl-C per terminare."
st = threading.Thread( target = s.serve_forever )
st.start()

try :
    while 1 :
        time.sleep(0.2)

except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    print "In attesa della chiusura del server"
    st.join() 
    print "Fatto!"
        
