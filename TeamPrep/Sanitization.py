# Project: Brewing Automation System - Capstone Project
# Purpose Details: Sanitization class - To ask user if sanitization is completed
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/18
# Rev

# import RPi.GPIO as GPIO
import time
import datetime
from Brewing.Log import Log
from Brewing.ServiceNowLog import ServiceNowLog



# button for sanitization
# s_button_pin = 26 # UP key

# Pin setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(s_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

class Sanitization:

    # def __init__(self,button):
    #    '''
    #   Defines attributes of sanitization
    #   '''
    #    self.button = button
    #   '''
    #  Adds method to the attribute for sanitization
    #    '''

    '''
    logging for sanitation
    '''
    def sanitization(self, request_number):

        time.sleep(3)
        input("\033[1m" + "\n    1. Press Enter when sanitization is done:" + "\033[0m \n")
        # GPIO.wait_for_edge(self.button,GPIO.FALLING)
        time.sleep(1)
        message = ("   Sanitization Completed. ")
        print("\t\t" + message + "\n")
        try:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Sanitization\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Prep.Sanitization", "Sanitization done.", datetime.datetime.now(), "pass")
            print(log.generate_log())
            time.sleep(2)
        except Exception as e:
            print(e)


# # USAGE
# s = sanitization(s_button_pin)
# try:
#     s.button_fun()
# except:
#     GPIO.cleanup()
# GPIO.cleanup()