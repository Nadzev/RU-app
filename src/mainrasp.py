# bibliotecas que nao precisam de versionamento 
import time 
from subprocess import Popen, PIPE
from datetime import datetime

# bibliotecas especificas do rasp 
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from  gpiozero import Servo

# setando as portas e tamanho do LCD 
# seria bom isso ficar em outro arquivo..
lcd_columns = 16
lcd_rows = 2
lcd_rs = digitalio.DigitalInOut(board.D4)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d7 = digitalio.DigitalInOut(board.D22)

# instanciacoes
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)
servo = Servo(6) # 6 eh o GPIO que ele ta conectado 
reader = SimpleMFRC522()
LEDvermelho = digitalio.DigitalOut(board.D26)
LEDverde = digitalio.DigitalOut(board.D16)
LEDvermelho.direction = digitalio.Direction.OUTPUT
LEDverde.direction = digitalio.Direction.OUTPUT

horaatual  = datetime.now()

# setup inicial 
lcd.message = "------- RU ------- \n Passe um cartão!"
servo.min()
LEDverde.value = True

# loop 
try:
	while True:
		id, _ = reader.read()
		print(id," ",type(id))
		print("\n",str(id), " ", type(id))
finally:
        print("acabou")