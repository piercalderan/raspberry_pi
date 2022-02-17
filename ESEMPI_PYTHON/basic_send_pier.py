# Esempio di trasmissione OSC. Pier Calderan 2015
# -*- coding: utf-8 -*-
import OSC
import time
send_address = '192.168.1.99', 9000
c = OSC.OSCClient()
c.connect( send_address ) 
msg = OSC.OSCMessage()
msg.setAddress("/1/label1")
msg.append( "ETICHETTA" ) 
c.send(msg) 
time.sleep(1)

try :
    while 1:
        msg = OSC.OSCMessage()
        msg.setAddress("/1/fader1")
        msg.append(50.1)
        c.send(msg) 
        time.sleep(1) 

        msg = OSC.OSCMessage()
        msg.setAddress("/1/fader1")
        msg.append(10.0)
        c.send(msg) 
        time.sleep(1)
        
except KeyboardInterrupt:
    print "Chiusura del client OSC"
    c.close()
    print "Fatto!"        
