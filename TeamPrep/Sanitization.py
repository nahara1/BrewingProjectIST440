# Project: Brewing Automation System - Capstone Project
# Purpose Details: Sanitization class - To ask user if sanitization is completed
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/22
# Rev 3

# import RPi.GPIO as GPIO
import time
import datetime
from Brewing.Log import Log
from Brewing.ServiceNowLog import ServiceNowLog


# noinspection PyMethodMayBeStatic
class Sanitization:

    # noinspection PyMethodMayBeStatic
    def __init__(self):
        self.log_no = 0

    def sanitization(self, request_number):
        try:
            time.sleep(1)
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Sanitization\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no, "Prep.Sanitization", "Asked for manual input if Sanitization completed.",
                      datetime.datetime.now(),
                      "pass")
            print(log.generate_log())
            time.sleep(2)
            input("\033[1m" + "\n    1. Press Enter when sanitization is done:" + "\033[0m \n")
            # GPIO.wait_for_edge(self.button,GPIO.FALLING)
            time.sleep(1)
            # noinspection PyRedundantParentheses
            message = ("   Sanitization Completed.\n")
            print("\t\t" + message + "\n")
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Sanitization\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no, "Prep.Sanitization", "Sanitization done - Input received.", datetime.datetime.now(),
                      "pass")
            print(log.generate_log())
            time.sleep(2)
        except Exception as e:
            print(e)
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Sanitization\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(int(self.log_no), "Prep.Sanitization", "Input for Sanitization completed failed.",
                      datetime.datetime.now(),
                      "fail")
            print(log.generate_log())
            time.sleep(2)
        return self.log_no