#!/usr/bin/python3
#Author: Simon Fukada
#Purpose: switches between Red and Green LED when button is pressed and released
import RPi.GPIO as GPIO
import time

outpinRed = 11
outpinGreen = 13
inputpin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(outpinRed, GPIO.OUT)
GPIO.setup(outpinGreen, GPIO.OUT)
GPIO.setup(inputpin, GPIO.IN)

changeLight = True
switchLight = True

try:
    while(True):
        if(GPIO.input(inputpin) == True):
            print("Button up first loop")
            GPIO.output(outpinRed, GPIO.LOW)
            GPIO.output(outpinGreen, GPIO.LOW)
            while(GPIO.input(inputpin) == True):
                print("Button up second loop")
                if(changeLight):
                    switchLight = False
                else:
                    switchLight = True
        else:
            while(GPIO.input(inputpin) == False):
                if(switchLight):
                    print("Red Light")
                    GPIO.output(outpinRed, GPIO.HIGH)
                    changeLight = True
                else:
                    print("Green Light")
                    GPIO.output(outpinGreen, GPIO.HIGH)
                    changeLight = False
            
except:
    print("Goodbye, the program is ending")
finally:
    GPIO.cleanup()
