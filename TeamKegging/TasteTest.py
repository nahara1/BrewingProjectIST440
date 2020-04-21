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
        """
        Method that returns the status of the Taste Test object

        :return: String format status report
        """
        return "Taste Test ID: {}\n" \
               "Taster Name: {}\n" \
               "Taster ID: {}\n" \
               "Taste Test Status: {}\n".format(self.tt_id, self.taster_name, self.taster_id, self.tt_status)

    def tt_log(self, batch_id, bb_stage, log_message):
        """

        :param batch_id: batch_id or request_id of the current beer batch
        :param bb_stage: current stage in the brewing Process
        :param log_message: the message or log that will be sent to service now or appened to the log list
        :return: sends a log with timestamp to ServiceNow and appends to the log list
        """
        try:
            currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(
                bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " + str(log_message) + "\"}"

            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            tt_loglist.append(status_log)
        except Exception as e:
            print("Taste Test Logging error:" + str(e))

    def record_quality(self, batch_id):
        """
        Method called in Taste Test to record a tester name, RFID and quality report prompt with a log.

        :param batch_id: The batch_id or request_id of the current beer batch
        :return: None.
        """
        try:

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
                print("Name: " + tt_taster + " RFID: " + tt_taster_id)
                print()
                print(tt_quality)
                print("")
                choice = input("Is this correct (Y/N): ")
                if choice in ['Y', 'y', 'yes', 'Yes', 'YES']:
                    report_correct = True
                    self.tt_status = "QA_TASTING"
                    beer_report = "Quality Assurance Beer Quality Report:: " + "Name: " + tt_taster + " RFID: " + tt_taster_id + tt_quality
                    self.tt_log(batch_id, "Kegging", beer_report)
                elif choice in ['N', 'n', 'no', 'No', 'NO']:
                    pass
        except Exception as e:
            print("Quality Report Entry Error: " + str(e))

    def record_ibu(self, batch_id, recipe_ibu):
        """
        Method called in Taste Test to prompt and store a Taster and IBU report.
        :param batch_id: the current Batch ID or Request ID of the current beer batch
        :param recipe_ibu: the required IBU target given by a recipe
        :return: None.
        """
        try:
            ibu_correct = False
            while not ibu_correct:
                print()
                print("This is the IBU Report")
                print("The target IBU (International Bitterness Unit) Score is (" + str(recipe_ibu) + ").")
                print()
                tt_taster = input("Enter your name: ")
                tt_taster_id = input("Enter you RFID number: ")
                ibu = float(
                    input("Please enter the IBUs (International Bitterness Units) for beer batch (Batch_ID: " + str(
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
                    ibu_report = "Quality Assurance IBU Report:: " + "Name: " + tt_taster + " RFID: " + tt_taster_id + " IBU: " + str(
                        ibu)
                    self.tt_log(batch_id, "Kegging", ibu_report)
                elif choice in ['N', 'n', 'no', 'No', 'NO']:
                    pass
        except Exception as e:
            print("IBU Report Input Error: " + str(e))

    def quality_pass_fail(self, batch_id):
        """
        Method that is called in Taste Test to confirm the final pass/fail or a beer batch with log.
        :param batch_id: the current Batch ID or Request ID of the current beer batch
        :return: None
        """
        try:
            quality_pass = False
            while not quality_pass:
                self.record_quality(batch_id)
                result = input("This is the Final QA Pass Fail Result" + "\n" + "Does beer batch (Batch_ID: " + str(
                    batch_id) + ") pass Quality Assurance Inspection (Y/N): ")
                if result in ['Y', 'y', 'yes', 'Yes', 'YES']:
                    quality_pass = True
                    qa_report = "Quality Assurance: Beer Quality Test Passed."
                    self.tt_log(batch_id, "Kegging", qa_report)
                elif result in ['N', 'n', 'no', 'No', 'NO']:
                    pass
        except Exception as e:
            print("Final QA Test Input Error: " + str(e))

    def tt_main(self, batch_id, recipe_ibu):  # kegging task start
        """
        Main Taste Test method that calls the QA, IBU, and Pass/Fail methods and logs.

        :param batch_id: the current Batch ID or Request ID of the current beer batch
        :param recipe_ibu: the required IBU target given by a recipe
        :return: None. Logs all Taste Test events
        """

        # list of tasks unused, here for reminder
        # t1 = '1. Record Beer Quality'
        # t2 = '2. Record IBU (International Bitterness Units)'
        # t3 = '3. P / F'

        try:
            self.tt_status = "QA_START"
            self.tt_log(batch_id, "Kegging", "Taste Test In Progress")

            self.record_ibu(batch_id, recipe_ibu)
            self.quality_pass_fail(batch_id)

            self.tt_log(batch_id, "Kegging", "Ready for Kegging Tasks")
        except Exception as e:
            print("Taste Test Process Error: " + str(e))

    def get_tt_loglist(self):
        """
        Method that returns the log list of Taste Test events
        :return: list of log events from Taste Test
        """
        return tt_loglist

# tt1 = TasteTest(1,"Daibo",1111,"QA_START",0)
# tt1.tt_main(1,38.5)
# for n in tt1.get_tt_loglist():
#    print(n)
