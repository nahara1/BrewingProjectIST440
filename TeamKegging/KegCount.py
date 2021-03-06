# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - Keg Class
# Course: IST 440W - 001
# Author: Daibo Zhang
# Date Developed: 4/18/2020
# Last Date Changed: 4/18/2020
# Rev: 1.0

import sys
from TeamKegging.Keg import Keg
from Brewing import ServiceNowLog
from Brewing import MongoLogging
import datetime

kc_loglist = []


class KegCount:
    def __init__(self, batch_id, kc_status):
        self.batch_id = batch_id
        self.kc_status = kc_status

    def get_status(self):
        """
        Method that returns the status of the Keg Count process
        :return: String format of the status of the Keg Count object
        """
        return "Batch ID: {}\n" \
               "Final Status: {}\n".format(self.batch_id, self.kc_status)

    def kc_log(self, batch_id, bb_stage, log_message):
        """
        Logging Method for the Keg Count

        :param batch_id: The batch ID of the current batch
        :param bb_stage: The current Brewing Stage
        :param log_message: The main log message
        :return: Sends a log to ServiceNow with timestamp appended to the beginning of the log message

        """
        try:
            currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(
                bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " + str(log_message) + "\"}"
            ServiceNowLog.ServiceNowLog.create_new_log(ServiceNowLog.ServiceNowLog(), status_log)
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, batch_id, "Kegging", log_message)
            kc_loglist.append(status_log)
        except Exception as e:
            print("Keg Count Log Error:  " + str(e))

    def kc_confirm_batch(self):
        """
        Method called in Keg Count process that confirms the batch ID of the current beer batch. Logs events
        :return: None.
        """
        try:
            batch_confirm = False

            while not batch_confirm:
                print("")
                print("Starting Keg Count Tasks. The current batch is (Batch ID: " + str(self.batch_id) + ").")
                save_batch_id = input("Please confirm the batch ID: ")  # user input for batch ID
                confirm_batch_id = input("Are you sure? Enter (y/n): ")
                if confirm_batch_id in ['Y', 'y', 'yes', 'Yes', 'YES']:
                    self.kc_log(self.batch_id, "Kegging",
                                "Keg Count: Counting Final kegs for Batch ID: " + save_batch_id)  # logging to service now
                    batch_confirm = True
                elif batch_confirm in ['N', 'n', 'no', 'No', 'NO']:
                    pass
                else:
                    print("Confirmation failed. Please try again.")
                    self.kc_log(self.batch_id, "Kegging",
                                "Keg Count: Batch ID Confirmation Error")  # logging to service now
                    print()
        except Exception as e:
            print("Keg Count Batch Confirm Error " + str(e))

    def input_keg_id(self):
        """
        Asks the user to input the Keg ID.
        :return: User input Keg ID
        """
        return input("Enter the Keg ID: ")

    def input_keg_volume(self):
        """
        Asks the user to input the beer volume.
        :return: User input Beer Volume
        """
        return float(input("Enter the Beer Volume: "))

    def input_keg_pressure(self):
        """
        Asks the user to input the Keg Pressure.
        :return: User input keg pressure
        """
        return float(input("Enter the Keg Pressure (PSI): "))

    def input_keg_style(self):
        """
        Method that returns a keg style based off user input
        :return: Keg Type KEG_SIXTEL, KEG_QUARTER_STUBBY, or KEG_QUARTER_SLIM
        """
        try:
            answer = input("Enter the Keg Type \n(1) for Sixtel \n(2) for Quarter Stubby \n(3) for Quarter Slim \n"
                           "Enter your selection here: ")
            if answer in ['1', 'Sixtel', 'sixtel', "SIXTEL"]:
                return "KEG_SIXTEL"
            elif answer in ['2', 'Quarter Stubby', 'QUARTER STUBBY', 'quarter stubby', 'stubby', 'Stubby', 'STUBBY']:
                return "KEG_QUARTER_STUBBY"
            elif answer in ['3', 'Quarter Slim', 'QUARTER SLIM', 'quarter slim', 'slim', 'Slim', 'SLIM']:
                return "KEG_QUARTER_SLIM"
            else:
                print("Please Enter a valid Keg Style")
        except Exception as e:
            print("Keg Style Input Error: " + str(e))

    def kc_new_keg(self):
        """
        Method that asks the user to enter information for a new Keg object

        :return: returns the information in string format of the new keg
        """

        try:
            new_id = self.input_keg_id()
            new_style = self.input_keg_style()
            new_vol = self.input_keg_volume()
            new_pressure = self.input_keg_pressure()

            new_keg = Keg(new_id, "DEFAULT", new_vol, new_pressure, "DEFAULT")

            if new_style == "KEG_SIXTEL":
                new_keg.set_style_sixtel()
            elif new_style == "KEG_QUARTER_STUBBY":
                new_keg.set_style_quarter_stubby()
            elif new_style == "KEG_QUARTER_SLIM":
                new_keg.set_style_quarter_slim()
            else:
                pass
            return new_keg.get_info()
        except Exception as e:
            print("Keg Count New Keg Entry Error: " + str(e))

    def kc_count_kegs(self):
        """
        Method called in the Keg Count process that confirms the number of kegs in the batch. Logs events
        :return: None
        """
        try:
            kc_done = False
            kc_f_count = 0
            while not kc_done:
                kc_count = int(
                    input("Please enter the number of kegs for beer batch (Batch_ID: " + str(self.batch_id) + "): "))
                print("")
                print("The number of kegs you have entered is as follows:")
                print("")
                print(str(kc_count))
                print("")

                kc_choice = input("Is this correct (Y/N): ")

                if kc_choice in ['Y', 'y', 'yes', 'Yes', 'YES']:
                    self.kc_status = "KEG_COUNT_COUNTED"
                    kc_f_count = kc_count
                    kc_report = "Final Keg Count: " + str(kc_count) + " Keg(s)"
                    self.kc_log(self.batch_id, "Kegging", kc_report)
                    kc_done = True
                elif kc_choice in ['N', 'n', 'no', 'No', 'NO']:
                    pass
            return kc_f_count
        except Exception as e:
            print("Keg Count Count Error: " + str(e))

    def kc_record_keg_id(self):
        """
        Main Method call that confirms the completion of Keg Count process and logs
        :return: None. calls kc_log method
        """
        keglist = []
        keg_num = 0

        total_kegs = self.kc_count_kegs()

        try:
            while keg_num < total_kegs:
                keg_num += 1
                print("---------------------------------------")
                print("Keg " + str(keg_num) + ". ")
                print("---------------------------------------")
                print()
                print("Enter the information for Keg " + str(keg_num) + " ")

                confirm = 'N'
                while confirm not in ['Y', 'y', 'Yes', 'yes', 'YES']:
                    print("Keg " + str(keg_num) + ". ")
                    new_keg = self.kc_new_keg()
                    print()
                    print("Keg " + str(keg_num) + ". " + "\n" + str(new_keg))
                    confirm = input("Is this correct? (Y/N)")
                    if confirm in ['Y', 'y', 'Yes', 'yes', 'YES']:
                        keglist.append(new_keg)
                kc_log_message = "Keg Count: " + str(keg_num) + ' / ' + str(total_kegs) + " Kegs Recorded"
                self.kc_log(self.batch_id, "Kegging", kc_log_message)
            print("---------------------------------------")
        except Exception as e2:
            print("Keg ID Error: " + str(e2))

        for n in keglist:
            print(n)

        try:
            print("All Kegs for Batch (" + str(self.batch_id) + ") Counted and Ready")
            print("All Kegging Processes for Batch (" + str(self.batch_id) + ") Complete")
            self.kc_log(self.batch_id, "Kegging", "All Kegging Processes Complete")
            self.kc_log(self.batch_id, "Kegging", "Keg List:" + str(keglist))
        except Exception as e3:
            print("Keg Count Listing Error: " + str(e3))

    def get_kc_loglist(self):
        """
        Method that returns list of log events occurring in Keg Count Process
        :return: list of log events
        """
        return kc_loglist

    def kc_main(self):
        """
        Main Keg Count function Call
        :return: None
        """
        try:
            print()
            print("Starting Keg Count Process:")
            print()
            print()
            self.kc_confirm_batch()
        except Exception as confirm_error:
            print("Batch Confirmation Method Error :" + str(confirm_error))

        try:
            self.kc_record_keg_id()
        except Exception as record_error:
            print("Keg Record Error: " + str(record_error))


#kc1 = KegCount(1234, "KEG_COUNT_READY")
#kc1.kc_main()
