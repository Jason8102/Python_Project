#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
reader = SimpleMFRC522()

try:
    while True:
        #id, text = reader.read()
        id = reader.read_id()
        print(id)
        #print(text)
finally:
        GPIO.cleanup
