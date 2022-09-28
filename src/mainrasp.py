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
LEDvermelho = 37 # Vamos utilizar o pino 36 da placa
LEDverde = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDvermelho, GPIO.OUT)
GPIO.setup(LEDverde, GPIO.OUT)

# setup inicial 
lcd.message = "---------- RU ---------- \n Passe um cartão!"
servo.min()
GPIO.output(LEDverde, True) 

# loop 
try:
	while True:
		id, _ = reader.read()
		print(id," ",type(id))
		print("\n",str(id), " ", type(id))
finally:
        GPIO.cleanup()
        
tempo = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime()) # "28-09-2022 13:21:19" <- exemplo

print(tempo)