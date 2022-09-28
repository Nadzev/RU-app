# BIBLIOTECAS 
import time 

from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2
lcd_rs = digitalio.DigitalInOut(board.D4)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d7 = digitalio.DigitalInOut(board.D22)

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)
lcd.message("OOOOOOOOOOOOI")

# def setup():


# tempo = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
# print(tempo)