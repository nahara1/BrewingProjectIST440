# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - Keg Class
# Course: IST 440W - 001
# Author: Daibo Zhang
# Date Developed: 4/18/2020
# Last Date Changed: 4/18/2020
# Rev: 1.0

from TeamKegging.Keg import Keg
from Brewing import ServiceNowLog
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
        currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(
            bb_stage) + "\", \"log\":\"" + str(log_message) + "\"}"

        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        kc_loglist.append(status_log)

    def kc_confirm_batch(self):
        while True:
            # logging to service now
            print("")
            print("Starting Cellarman Tasks. The current batch is (Batch ID: " + str(self.batch_id) + ").")
            save_batch_id = input("Please confirm the batch ID: ")  # user input for batch ID
            confirm_batch_id = input("Are you sure? Enter (y/n): ")
            if confirm_batch_id == 'y':
                self.kc_log(self.batch_id, "Kegging",
                            "Keg Count: Batch ID entered as: " + save_batch_id)  # logging to service now
                break
            else:
                print("Confirmation failed. Please try again.")
                self.kc_log(self.batch_id, "Kegging",
                            "Keg Count: Batch ID Confirmation Mismatch")  # logging to service now
                print()
            self.kc_log(self.batch_id, "Kegging", "Keg Count: Counting final Kegs")

    def kc_count_kegs(self):
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
                self.kc_status = "KEG_COUNT_FINISHED"
                kc_f_count = kc_count
                kc_report = "Final Keg Count: " + str(kc_count) + " Keg(s)"
                self.kc_log(self.batch_id, "Kegging", kc_report)
                kc_done = True
            elif kc_choice in ['N', 'n', 'no', 'No', 'NO']:
                pass
        return kc_f_count

    def input_keg_id(self):
        """
        Asks the user to input the Keg ID.
        This function returns nothing.
        """
        return input("Enter the Keg ID: ")

    def input_keg_volume(self):
        """
        Asks the user to input the beer volume.
        This function returns nothing.
        """
        return float(input("Enter the Beer Volume: "))

    def input_keg_pressure(self):
        """
        Asks the user to input the Keg Pressure.
        This function returns nothing.
        """
        return float(input("Enter the Keg Pressure (PSI): "))

    def input_keg_style(self):
        while True:
            answer = input("Enter the Keg Type (Sixtel/Quarter Stubby/Quarter Slim): ")
            if answer in ['Sixtel', 'sixtel', "SIXTEL"]:
                return "KEG_SIXTEL"
            elif answer in ['Quarter Stubby', 'QUARTER STUBBY', 'quarter stubby', 'stubby', 'Stubby', 'STUBBY']:
                return "KEG_QUARTER_STUBBY"
            elif answer in ['Quarter Slim', 'QUARTER SLIM', 'quarter slim', 'slim', 'Slim', 'SLIM']:
                return "KEG_QUARTER_SLIM"
            else:
                print("Please Enter a valid Keg Style")

    def kc_new_keg(self):
        """
        Method that asks the user to enter information for a new Keg object
        :param new_id: Keg ID for the new Keg
        :param new_style: Keg Type for the new keg
        :param new_vol: Beer Volume for the Keg
        :param new_pressure: Keg Final Pressure
        :return: returns the information in string format of the new keg
        """

        new_id = self.input_keg_id()
        new_style = self.input_keg_style()
        new_vol = self.input_keg_volume()
        new_pressure = self.input_keg_pressure()


        new_keg = Keg(new_id, "DEFAULT", new_vol, new_pressure, "DEFAULT")

        if new_style == "KEG_SIXTEL":
            new_keg.set_style_sixtel()
        elif new_style == "KEG_QUARTER_STUBBY":
            new_keg.set_style_quater_stubby()
        elif new_style == "KEG_QUARTER_SLIM":
            new_keg.set_style_quarter_slim()
        return new_keg.get_info()

    def kc_record_keg_id(self):
        kc_done = False
        keglist = []
        keg_num = 0
        total_kegs = self.kc_count_kegs()
        while keg_num < total_kegs:
            keg_num += 1
            print("---------------------------------------")
            print("Keg " + str(keg_num) + ". ")
            print("---------------------------------------")
            print()
            print("Enter the information for Keg " + str(keg_num) + " ")

            confirm = 'N'
            while not confirm in ['Y', 'y', 'Yes', 'yes', 'YES']:
                print("Keg " + str(keg_num) + ". ")
                new_keg = self.kc_new_keg()
                print()
                print("Keg " + str(keg_num) + ". " + "\n" + str(new_keg))
                confirm = input("Is this correct? (Y/N)")
            keglist.append(new_keg)
            kc_log_message = "Keg Count: " + str(keg_num) + ' / ' + str(total_kegs) + " Kegs Recorded"
            self.kc_log(self.batch_id, "Kegging", kc_log_message)
        print("---------------------------------------")
        while not kc_done:
            for n in keglist:
                print(n)
            kc_done = True
        print("All Kegs for Batch (" + str(self.batch_id) + ") Counted and Ready")
        print("All Kegging Processes for Batch (" + str(self.batch_id) + ") Complete")
        self.kc_log(self.batch_id, "Kegging", "All Kegging Processes Complete")
        self.kc_log(self.batch_id, "Kegging", "Keg List:" + str(keglist))

    def get_kc_loglist(self):
        return kc_loglist

    def kc_main(self):
        self.kc_confirm_batch()
        self.kc_record_keg_id()

# kc1 = KegCount(1234, "KEG_COUNT_READY")
# kc1.kc_main()
