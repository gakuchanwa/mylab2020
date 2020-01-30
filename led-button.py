#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import subprocess

LedPin = 15    # pin15 --- led
BtnPin = 11    # pin12 --- button

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off

def loop():
    s = 0
    while True:
        if GPIO.input(BtnPin) == GPIO.LOW: # Check whether the button is pressed.
            print ('...led on')
            GPIO.output(LedPin, GPIO.LOW)  # led on
            if s == 0:
                print ( ' Photo ')
                result = subprocess.run(('$HOME/project/main/rpicamera.sh'),shell=True)
                s = 1
            else:
                print ( ' 2nd ')
        else:
            print ('led off...')
            s = 0
            GPIO.output(LedPin, GPIO.HIGH) # led off
        time.sleep(0.5)

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource
    print('-- cleanup GPIO!! --')

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()