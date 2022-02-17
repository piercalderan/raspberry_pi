# -*- coding: utf-8 -*-
# Display LCD. Pier Calderan 2015.
# 16 caratteri x 2 righe

import RPi.GPIO as GPIO
import time

# Definizione delle variabili dei pin del display per le porte GPIO
LCD_RS = 16	# Pin RS del display collegato a GPIO16
LCD_E  = 12	# Pin E del display collegato a GPIO12
LCD_DB4 = 25	# Pin D4 del display collegato a GPIO25
LCD_DB5 = 24	# Pin D5 del display collegato a GPIO24
LCD_DB6 = 23	# Pin D6 del display collegato a GPIO23
LCD_DB7 = 18	# Pin D7 del display collegato a GPIO18

# Definizione di alcune costanti del display
LCD_WIDTH = 16	# Caratteri del display
LCD_CHR = True	# Carattere
LCD_CMD = False	# Comando
LCD_LINE_1 = 0x80	# Indirizzo RAM del display per la prima riga
LCD_LINE_2 = 0xC0	# Indirizzo RAM del display per la seconda riga

# Costanti del clock (Timing)
E_PULSE = 0.00005
E_DELAY = 0.00005

# Definizione del programma Main
def main():
  GPIO.setmode(GPIO.BCM)	# Imposta la modalità BCM
  GPIO.setup(LCD_E, GPIO.OUT)	# Imposta la porta E in uscita
  GPIO.setup(LCD_RS, GPIO.OUT)  # Imposta la porta RS in uscita
  GPIO.setup(LCD_DB4, GPIO.OUT) # Imposta la porta DB4 in uscita
  GPIO.setup(LCD_DB5, GPIO.OUT) # Imposta la porta DB5 in uscita
  GPIO.setup(LCD_DB6, GPIO.OUT) # Imposta la porta DB6 in uscita
  GPIO.setup(LCD_DB7, GPIO.OUT) # Imposta la porta DB7 in uscita
  
  
# Chiama la funzione di inizializzazione del display
  lcd_init()

# Stampa di alcuni testi
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("Raspberry Pi")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("Hello World!")

  time.sleep(3)	# Ritardo di 3 secondi

# Altri testi di prova
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("Prima riga sopra")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("Seconda riga....")

  time.sleep(3) 	# Ritardo di 3 secondi
  print ("Cleanup!")  
  GPIO.cleanup()
  
  
# Funzione di inizializzazione del display
def lcd_init():
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)  
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)  

# Funzione di invio del  messaggio
def lcd_string(message):

# Il metodo ljust di Python restituisce la stringa giustificata a sinistra
  message = message.ljust(LCD_WIDTH," ")
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
             
def lcd_byte(bits, mode):
  # Manda i byte ai pin di dati DB4-DB7
  # bit = data
  # mode = True  per il carattere, False per il comando

  GPIO.output(LCD_RS, mode) # modalità RS

# Bit High
  GPIO.output(LCD_DB4, False)
  GPIO.output(LCD_DB5, False)
  GPIO.output(LCD_DB6, False)
  GPIO.output(LCD_DB7, False)
  
  if bits&0x10==0x10:
    GPIO.output(LCD_DB4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_DB5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_DB6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_DB7, True)

# Abilita il pin Enable
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)      

# Bit Low
  GPIO.output(LCD_DB4, False)
  GPIO.output(LCD_DB5, False)
  GPIO.output(LCD_DB6, False)
  GPIO.output(LCD_DB7, False)

  if bits&0x01==0x01:
    GPIO.output(LCD_DB4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_DB5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_DB6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_DB7, True)

# Abilita il pin Enable
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)   
  
if __name__ == '__main__':
  main()
# EOF
