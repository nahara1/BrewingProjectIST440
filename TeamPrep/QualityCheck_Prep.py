# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for implementing quality assurance
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/18/20
# Last Date Changed: 4/18/2020
# Rev 10

# Import Statements

from Brewing.ServiceNowLog import ServiceNowLog
import time
from Brewing.Log import Log
import datetime
from Brewing import MongoLogging
from TeamPrep.WeightScale import WeightScale

w = WeightScale()

class QualityCheck:

    # noinspection PyMethodMayBeStatic
    def __init__(self):
        self.log_no = w.log_no

    def get_QA_Check(self, request_number):
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"QualityCheck_Prep\"}"
        sn_log = ServiceNowLog()
        ServiceNowLog.create_new_log(sn_log, status_log)
        self.log_no = self.log_no + 1
        log = Log(self.log_no + 1, "Prep.QualityCheck", " Prep quality check started.",
                  datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.QualityCheck",
                                           "Prep quality check started.")
        time.sleep(1)
        print("Please Inspect the Prep Quality Before Start Brewing to Check if it Meets CGMP Standards: \n")
        # save text as variable
        quality_checked = ""
        while quality_checked != "Yes" or quality_checked != "No":
            if quality_checked == "Yes":
                print("Logging to ServiceNow...")
                time.sleep(1)
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"QualityCheck_Prep\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                self.log_no = self.log_no + 1
                log = Log(self.log_no, "Prep.QualityCheck", " Prep quality check: Passed QA.",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                ml = MongoLogging.MongoLogging()
                MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.QualityCheck",
                                                   "Prep quality check: Passed QA.")
                time.sleep(1)
                print("Successfully logged that Prep processes has completed and passes Quality Assurance.")
                time.sleep(1)
                break
            elif quality_checked == "No":
                print("Logging to ServiceNow...")
                time.sleep(1)
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"QualityCheck_Prep\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                self.log_no = self.log_no + 1
                log = Log(self.log_no, "Prep.QualityCheck", " Prep quality check: Failed QA.",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                ml = MongoLogging.MongoLogging()
                MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.QualityCheck",
                                                   "Prep quality check: Failed QA.")
                time.sleep(1)
                print("\nQuality Did not Pass, make correction and inspect again.\n")
                quality_checked = ""
                time.sleep(1)
            else:
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"QualityCheck_Prep\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                self.log_no = self.log_no + 1
                log = Log(self.log_no, "Prep.QualityCheck"," Prep quality check failed and need correction .",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                ml = MongoLogging.MongoLogging()
                MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.QualityCheck",
                                                   "Prep check failed and need correction.")
                text = input("\nPlease Enter Yes or No: ")
                quality_checked = text

