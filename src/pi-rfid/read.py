#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
	while True:
		id, _ = reader.read()
		print(id," ",type(id))
		print("\n",str(id), " ", type(id))
finally:
        GPIO.cleanup()
