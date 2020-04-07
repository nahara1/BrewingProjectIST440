# Project: Brewing Automation System - Capstone Project
# Purpose Details: Sanitization
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/5
# Rev

import RPi.GPIO as GPIO

# button for sanitization
s_button_pin = 26 # UP key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(s_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

class Sanitization:
    def __init__(self,button):
        self.button = button

    def button_function(self):
        print("\n      Press up button when sanitization is done.")
        GPIO.wait_for_edge(self.button,GPIO.FALLING)
        message = '  Sanitization    Completed'
        print("\t\t" + message)

# # USAGE
# s = sanitization(s_button_pin)
# try:
#     s.button_fun()
# except:
#     GPIO.cleanup()
# GPIO.cleanup()