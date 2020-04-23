# Project: Brewing Automation System - Capstone Project
# Purpose Details: Temperature Class - To get the temperature of Yeast
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/18
# Rev 3


import random
import time
import datetime
from TeamPrep.Sanitization import Sanitization
from Brewing.Log import Log
from Brewing.ServiceNowLog import ServiceNowLog

s = Sanitization()
# noinspection PyMethodMayBeStatic
class Temperature:
    def __init__(self):
        self.log_no = s.log_no

    def read_temp(self, request_number):
        try:
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Temperature\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(int(self.log_no), "Prep.Temperature", "Waiting to measure temperature of yeast", datetime.datetime.now(), "pass")
            print(log.generate_log())
            time.sleep(2)
            temperature = random.randrange(55, 85, 1)
            input("\033[1m    2. Press Enter to measure temperature of yeast: \033[0m\n")
            time.sleep(3)
            print('\t\t\tTemp = \033[1m{0:0.0f}*\033[0;0m F'.format(temperature))
            time.sleep(2)
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Temperature\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(int(self.log_no) , "Prep.Temperature", "Temperature of yeast received", datetime.datetime.now(), "pass")
            print(log.generate_log())
            time.sleep(2)
            return temperature
        except Exception as e:
            print(e)
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Temperature\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(int(self.log_no), "Prep.Temperature", "Failed to check temperature of yeast", datetime.datetime.now(), "fail")
            print(log.generate_log())
            time.sleep(2)

    def yeast_temp(self, request_number):
        tmp = self.read_temp(request_number)
        # noinspection PyRedundantParentheses
        while (tmp > 80 or tmp < 60):
            try:
                print("\t\b***Temperature of yeast is out of range.***")
                print("  ***Bring another yeast and measure temperature again.*** \n")
                time.sleep(3)
                self.log_no += 1
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Temperature\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                log = Log(int(self.log_no), "Prep.Temperature", "Temperature of yeast is not in range.", datetime.datetime.now(),
                          "fail")
                print(log.generate_log())
                time.sleep(2)
            except Exception as e:
                print(e)
            tmp = self.read_temp(request_number)
        try:
            print("       Temperature of yeast is in range and ready to use.\n")
            time.sleep(2)
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Temperature\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(int(self.log_no), "Prep.Temperature", "Temperature of yeast measured.", datetime.datetime.now(), "pass")
            print(log.generate_log())
            time.sleep(2)
        except Exception as e:
            print(e)
            self.log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Temperature\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(int(self.log_no), "Prep.Temperature", "Failed to measure temperature of yeast", datetime.datetime.now(), "fail")
            print(log.generate_log())
            time.sleep(2)

