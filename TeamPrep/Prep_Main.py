# Project: Brewing Automation System - Capstone Project
# Purpose Details: Employee Class
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/5
# Rev

import RPi.GPIO as GPIO
from Sanitization import Sanitization
from Temperature import Temperature

# sensor = 11
pin = 4

# button for sanitization
s_button_pin = 26 # UP key
# button for temperature
t_button_pin = 13 # DOWN key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(s_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(t_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

s = Sanitization(s_button_pin)
t = Temperature(t_button_pin)

try:
    s.button_function()
    try:
        tmp = t.read_temp()
        while( tmp > 80 or tmp < 60):
            print("\t Temperature of yeast is out of range. \n")
            
            #print("      press down button to measure temperature of yeast: ")
            tmp = t.read_temp()
            # GPIO.wait_for_edge(t_button_pin, GPIO.FALLING)
        print("\t temperature of yeast is in range and ready to use.\n")
    except:
        GPIO.cleanup()
except:
    GPIO.cleanup()
