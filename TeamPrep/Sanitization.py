# Project: Brewing Automation System - Capstone Project
# Purpose Details: Sanitization class - To ask user if sanitization is completed
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/22
# Rev 3

import time
import datetime
from Brewing.Log import Log
from Brewing.ServiceNowLog import ServiceNowLog
from Brewing import MongoLogging

sleep_time = .25


# noinspection PyMethodMayBeStatic
class Sanitization:
    # noinspection PyMethodMayBeStatic

    log_no = 0

    def sanitization(self, request_number):
        """
        Main method that runs the sanitation process to clean equipment
        Completion is done by user pressing enter and sends logging to ServiceNOW throughout the process
        :param request_number:
        :return:
        """
        log_no = 0
        try:
            time.sleep(sleep_time)
            log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Sanitization\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(log_no, "Prep.Sanitization", "Asked for manual input if Sanitization completed.",
                      datetime.datetime.now(),
                      "pass")
            print(log.generate_log())
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.Sanitization", "Asked for manual input if Sanitization completed")
            time.sleep(sleep_time * 2)
            input("\033[1m" + "\n    1. Press Enter when sanitization is done:" + "\033[0m \n")
            # GPIO.wait_for_edge(self.button,GPIO.FALLING)
            time.sleep(sleep_time)
            # noinspection PyRedundantParentheses
            message = ("   Sanitization Completed.\n")
            print("\t\t" + message + "\n")
            log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Sanitization\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(log_no, "Prep.Sanitization", "Sanitization done - Input received.", datetime.datetime.now(),
                      "pass")
            print(log.generate_log())
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.Sanitization", "Sanitization done -Input received.")
            time.sleep(sleep_time * 2)
        except Exception as e:
            print(e)
            log_no += 1
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Sanitization\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(int(log_no), "Prep.Sanitization", "Input for Sanitization completed failed.",
                      datetime.datetime.now(),
                      "fail")
            print(log.generate_log())
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.Sanitization", "Input for Sanitization completed failed")
            time.sleep(sleep_time * 2)
        return log_no
