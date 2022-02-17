# Lettura di un sensore analogico tramite un pin GPIO. Pier Calderan 2015
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO, time
GPIO.setmode(GPIO.BCM)

def RC_time (PinRC): # definizione della funzione di lettura RC

  counter = 0 # variabile per il conteggio dei cicli di lettura

  GPIO.setup(PinRC, GPIO.OUT) # pin GPIO impostato in uscita

# Portando il pin GPIO a un livello basso, il condensatore si scarica
  GPIO.output(PinRC, GPIO.LOW)

  time.sleep(0.1) # ritardo di 0,1 secondi

  GPIO.setup(PinRC, GPIO.IN) # pin GPIO impostato in ingresso

# Conteggio delle volte in cui la tensione è un valore high
  while (GPIO.input(PinRC) == GPIO.LOW):
    counter += 1

  return counter

while True: # iterazione while per la stampa della lettura (counter)

# Misura del tempo tramite il pin GPIO 21

  print (RC_time(21))
