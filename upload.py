#!/usr/bin/env python3


import RPi.GPIO as GPIO
from time import sleep as delay
import sys
import os

hexFile = sys.argv[1]


print("begin")
resetPin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(resetPin, GPIO.OUT)


def reset():
    GPIO.output(resetPin, GPIO.HIGH)
    delay(0.02)
    GPIO.output(resetPin, GPIO.LOW)
    delay(0.02)
    GPIO.output(resetPin, GPIO.HIGH)
def avrUpload(binFile):
    command = "avrdude -v -p atmega328p -c arduino -P/dev/ttyAMA0 -b 57600 -D -U flash:w:/home/pi/avrdude/" + str(binFile) + ":i &"
    os.system(command)
    reset()



avrUpload(hexFile)
reset()
