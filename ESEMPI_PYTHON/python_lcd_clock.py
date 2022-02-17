# -*- coding: utf-8 -*-
# Display LCD 16 caratteri x 2 righe. Pier Calderan 2015.

import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BCM)	   # Imposta la modalità BCM

numero = time.strftime("%d")
giorno = int(time.strftime("%w"))
mese = int(time.strftime("%m"))
giorni = ["Dom", "Lun","Mar","Mer","Gio","Ven","Sab"]
mesi = ["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
anno = time.strftime("%Y")
ora = int(time.strftime("%H"))+2
minuti = time.strftime("%M")
secondi = time.strftime("%S")

giorno = str((giorni[giorno]))
mese = str((mesi[mese-1]))
ora = str(ora)
data = giorno +" "+ numero +" "+ mese +" "+ anno
print (data)
orario = ora + ":" + minuti + ":" + secondi
print (orario)

# Definizione delle variabili dei pin del display per le porte GPIO
LCD_RS = 16	# Pin RS del display collegato a GPIO16
LCD_E  = 12	# Pin E del display collegato a GPIO12
LCD_DB4 = 25	# Pin D4 del display collegato a GPIO25
LCD_DB5 = 24	# Pin D5 del display collegato a GPIO24
LCD_DB6 = 23	# Pin D6 del display collegato a GPIO23
LCD_DB7 = 18	# Pin D7 del display collegato a GPIO18
LCD_BUTTON = 21

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
  GPIO.setmode(GPIO.BCM)	   # Imposta la modalità BCM
  GPIO.setup(LCD_BUTTON, GPIO.IN)
  GPIO.setup(LCD_E, GPIO.OUT)	   # Imposta la porta E in uscita
  GPIO.setup(LCD_RS, GPIO.OUT)   # Imposta la porta RS in uscita
  GPIO.setup(LCD_DB4, GPIO.OUT) # Imposta la porta DB4 in uscita
  GPIO.setup(LCD_DB5, GPIO.OUT) # Imposta la porta DB5 in uscita
  GPIO.setup(LCD_DB6, GPIO.OUT) # Imposta la porta DB6 in uscita
  GPIO.setup(LCD_DB7, GPIO.OUT) # Imposta la porta DB7 in uscita
  GPIO.setwarnings(False) # Disabilita gli avvisi GPIO
  
  
# Funzione di inizializzazione del display
  lcd_init()
  while True:
    try:
      input_value=GPIO.input(21)
      time.sleep (1)
      if input_value==True:
        printout_on()
      elif input_value==False:
        printout_off()
    except KeyboardInterrupt:
      print ("Fine!")
      GPIO.cleanup()
      sys.exit(0)
      
# Stampa di alcuni testi
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("Raspberry Pi")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string(giorno)
  

  time.sleep(3)	# Ritardo di 3 secondi

# Altri testi di prova
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("Prima riga sopra")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string("Seconda riga....")
  
  time.sleep(3) 	# Ritardo di 3 secondi
  GPIO.cleanup()
  
# Inizializzazione del display
def lcd_init():
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)  
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)  

# Manda la stringa del messaggio
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
def printout_on():
  # Stampa il valore del pulsante on
  numero = time.strftime("%d")
  giorno = int(time.strftime("%w"))
  mese = int(time.strftime("%m"))
  giorni = ["Dom", "Lun","Mar","Mer","Gio","Ven","Sab"]
  mesi = ["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
  anno = time.strftime("%Y")
  giorno = str((giorni[giorno]))
  mese = str((mesi[mese-1]))
  data = giorno +" "+ numero +" "+ mese +" "+ anno
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("DATA UTC")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string(data)

def printout_off():
  # Stampa il valore del pulsante off
  ora = str(int(time.strftime("%H"))+2)
  minuti = time.strftime("%M")
  secondi = time.strftime("%S")
  data = giorno +" "+ numero +" "+ mese +" "+ anno
  orario = ora + ":" + minuti + ":" + secondi
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string("OROLOGIO UTC")
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string(orario)

if __name__ == '__main__':
  main()
# EOF
