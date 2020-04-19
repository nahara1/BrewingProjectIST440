# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - KeggingTask Class
# Course: IST 440W - 001
# Author: Aaleem Siddiqui, Daibo Zhang, Jun Baek
# Date Developed: 4/4/2020
# Last Date Changed: 4/18/2020
# Rev: 9


import datetime
from Brewing import ServiceNowLog


tt_loglist = []


class TasteTest:
    def __init__(self, tt_id, taster_name, taster_id, tt_status, tt_ibu):
        self.tt_id = tt_id
        self.taster_name = taster_name
        self.taster_id = taster_id
        self.tt_status = tt_status
        self.tt_ibu = tt_ibu

    def get_status(self):
        return "Taste Test ID: {}\n" \
               "Taster Name: {}\n" \
               "Taster ID: {}\n" \
               "Taste Test Status: {}\n".format(self.tt_id, self.taster_name, self.taster_id, self.tt_status)

    def tt_log(self, batch_id, bb_stage, log_message):
        currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(
            bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " + str(log_message) + "\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(ServiceNowLog, status_log)
        tt_loglist.append(status_log)

    def record_quality(self, batch_id):
        report_correct = False
        while not report_correct:
            print()
            print("This is the Quality Report")
            tt_taster = input("Enter your name: ")
            tt_taster_id = input("Enter you RFID number: ")
            tt_quality = input(
                "Please enter the beer quality report for beer batch (Batch_ID: " + str(batch_id) + "): ")
            print("")
            print("The report you have entered is as follows:")
            print("")
            print("Name: "+ tt_taster + " RFID: " + tt_taster_id)
            print()
            print(tt_quality)
            print("")
            choice = input("Is this correct (Y/N): ")
            if choice in ['Y', 'y', 'yes', 'Yes', 'YES']:
                report_correct = True
                self.tt_status = "QA_TASTING"
                beer_report = "Quality Assurance Beer Quality Report:: " + "Name: "+ tt_taster + " RFID: " + tt_taster_id + tt_quality
                self.tt_log(batch_id, "Kegging", beer_report)
            elif choice in ['N', 'n', 'no', 'No', 'NO']:
                pass

    def record_ibu(self, batch_id, recipe_ibu):
        ibu_correct = False
        while not ibu_correct:
            print()
            print("This is the IBU Report")
            print("The target IBU (International Bitterness Unit) Score is (" + str(recipe_ibu) + ").")
            print()
            tt_taster = input("Enter your name: ")
            tt_taster_id = input("Enter you RFID number: ")
            ibu = float(input("Please enter the IBUs (International Bitterness Units) for beer batch (Batch_ID: " + str(
                batch_id) + "): "))
            print()
            print("The IBUs you have entered is as follows:")
            print()
            print("Name: " + tt_taster + " RFID: " + tt_taster_id)
            print()
            print(str(ibu))
            print()
            choice = input("Is this correct (Y/N): ")
            if choice in ['Y', 'y', 'yes', 'Yes', 'YES']:
                self.tt_ibu = ibu
                ibu_correct = True
                self.tt_status = "QA_IBU_TASTING"
                ibu_report = "Quality Assurance IBU Report:: " + "Name: "+ tt_taster + " RFID: " + tt_taster_id  + str(ibu)
                self.tt_log(batch_id, "Kegging", ibu_report)
            elif choice in ['N', 'n', 'no', 'No', 'NO']:
                pass

    def quality_pass_fail(self, batch_id):
        quality_pass = False
        while not quality_pass:
            self.record_quality(batch_id)
            result = input( "This is the Final QA Pass Fail Result" + "\n" + "Does beer batch (Batch_ID: " + str(batch_id) + ") pass Quality Assurance Inspection (Y/N): ")
            if result in ['Y', 'y', 'yes', 'Yes', 'YES']:
                quality_pass = True
                qa_report = "Quality Assurance: Beer Quality Test Passed."
                self.tt_log(batch_id, "Kegging", qa_report)
            elif result in ['N', 'n', 'no', 'No', 'NO']:
                pass

    def tt_main(self, batch_id, recipe_ibu):  # kegging task start

        # list of tasks
        t1 = '1. Record Beer Quality'
        t2 = '2. Record IBU (International Bitterness Units)'
        t3 = '3. P / F'

        # declaring lists
        taskList = [t1, t2, t3]

        self.tt_status = "QA_START"
        self.tt_log(batch_id, "Kegging", "Taste Test In Progress")

        self.record_ibu(batch_id, recipe_ibu)
        self.quality_pass_fail(batch_id)

        self.tt_log(batch_id, "Kegging", "Ready for Kegging Tasks")

    def get_tt_loglist(self):
        return tt_loglist

tt1 = TasteTest(1,"Daibo",1111,"QA_START",0)
tt1.tt_main(1,38.5)
for n in tt1.get_tt_loglist():
    print(n)
