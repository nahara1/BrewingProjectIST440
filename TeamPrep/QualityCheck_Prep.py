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


class QualityCheck:

    # noinspection PyMethodMayBeStatic
    def get_QA_Check(self, request_number):
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"QualityCheck,Prep\"}"
        sn_log = ServiceNowLog()
        ServiceNowLog.create_new_log(sn_log, status_log)
        log = Log(20, "Prep.QualtyCheck", "Quality check started .",
                  datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        time.sleep(1)
        print("Please Inspect the Prep Quality Before Start Brewing to Check if it Meets CGMP Standards: \n")
        # save text as variable
        quality_checked = ""
        while quality_checked != "Yes" or quality_checked != "No":
            if quality_checked == "Yes":
                print("Logging to ServiceNow...")
                time.sleep(1)
                status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Preparation\", \"log\":\"Finished Prep process; Passed QA\"}"
                ServiceNowLog.create_new_log(sn_log, status_log)
                time.sleep(1)
                print("Successfully logged that Prep processes has completed and passes Quality Assurance.")
                time.sleep(1)
                break
            elif quality_checked == "No":
                print("Logging to ServiceNow...")
                time.sleep(1)
                status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Preparation\", \"log\":\"Prep stage; Failed QA\"}"
                ServiceNowLog.create_new_log(sn_log, status_log)
                time.sleep(1)
                print("Quality Did not Pass, make correction and inspect again.")
                quality_checked = ""
                time.sleep(1)
            else:
                text = input("\nPlease Enter Yes or No: ")
                quality_checked = text

