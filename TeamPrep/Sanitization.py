# Project: Brewing Automation System - Capstone Project
# Purpose Details: Sanitization class
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/7
# Rev

# import RPi.GPIO as GPIO
import time

"""
# button for sanitization
s_button_pin = 26 # UP key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(s_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
"""
class Sanitization:
    """
    def __init__(self,button):
        '''
        Defines attributes of sanitization
        '''
        self.button = button
        '''
        Adds method to the attribute for sanitization 
        '''
    """

    def sanitization(self):
        input("\033[1m" + "\n   \033[0;39;40m 1. Press Enter when sanitization is done:\033[0;0m" + "\033[0m \n")
        # GPIO.wait_for_edge(self.button,GPIO.FALLING)
        time.sleep(1)
        message = ("   \033[0;32;40mSanitization Completed.\033[0;0m ")
        print("\t\t" + message + "\n")
        time.sleep(2)


# # USAGE
# s = sanitization(s_button_pin)
# try:
#     s.button_fun()
# except:
#     GPIO.cleanup()
# GPIO.cleanup()