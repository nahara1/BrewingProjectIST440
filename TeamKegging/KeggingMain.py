# Project: Brewing Project
# Purpose Details: Main control for Kegging
# Course: IST 440W
# Author: Team Kegging
# Date Developed: 4/14/2020
# Last Date Changed: 4/18/2020
# Rev: 1.1

from TeamKegging.KeggingBriteTank import KeggingBriteTank
from TeamKegging.TasteTest import TasteTest
from TeamKegging.KeggingTasks import KeggingTasks
from TeamKegging.KegCount import KegCount
from Brewing import ServiceNowLog
import datetime

km_full_loglist = []


class KeggingMain:
    def __init__(self, batch_id, kegging_status, recipe_ibu):
        self.batch_id = batch_id
        self.kegging_status = kegging_status
        self.recipe_ibu = float(recipe_ibu)

    def keg_log(self, bb_stage, log_message):
        """
        Dynamic loging method
        :param bb_stage: The brew batch stage (Kegging)
        :param log_message: Log message
        :return: creates a log message in JSON string format
        """
        try:
            batch_id = self.batch_id
            currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(
                bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " + str(log_message) + "\"}"
            ServiceNowLog.ServiceNowLog.create_new_log(ServiceNowLog.ServiceNowLog(), status_log)
        except Exception as e:
            print("Kegging Main Logging Error: " + str(e))

    def brite_start(self):
        """
        Method that starts a brite tank (ID:1) with default temp 55F, 5 gallon limit
        :return: starts brite tank, logs to bt_loglist and appends to km_full_loglist
        """
        try:
            bt1 = KeggingBriteTank(1, 55, 5, 5, 0, "BRITE_START")  #
            bt1.start_brite_tank(self.batch_id)
            km_full_loglist.extend(bt1.get_bt_loglist())
        except Exception as e:
            print("Brite Tank Start Error: " + str(e))

    def qa_start(self, taster_name, taster_id, recipe_ibu):
        """
        Method that starts the taste test
        :return: Starts taste test and creates log to tt_loglist and appends to km_full_loglist
        """
        try:
            tt1 = TasteTest(self.batch_id, taster_name, taster_id, "QA_START", recipe_ibu)
            tt1.tt_main(self.batch_id, 38.5)
            km_full_loglist.extend(tt1.get_tt_loglist())
        except Exception as e:
            print("Taste Test Start Error: " + str(e))

    def kt_start(self):
        """
        Method that starts the cellarman tasks
        :return: Starts cellarman (kegging) tasks and logs to kt_loglist and appends to km_full_loglist
        """
        try:
            kt1 = KeggingTasks(self.batch_id, 'Cellarman tasks', 'TASK_START')
            kt1.keggingtasksmain()
            km_full_loglist.extend((kt1.get_kt_loglist()))
        except Exception as e:
            print("Kegging Tasks Start Error: " + str(e))

    def kc_start(self):
        try:
            kc1 = KegCount(self.batch_id, "KEG_COUNT_READY")
            kc1.kc_main()
            km_full_loglist.extend((kc1.get_kc_loglist()))
        except Exception as e:
            print("Keg Count Start Error" + str(e))

    def km_get_full_loglist(self):
        """
        Method that returns a list of all logs from Kegging process
        :return: List of log entries
        """
        return km_full_loglist

    def print_km_full_loglist(self):
        """
        Method that prints each individual entry in the full log list
        :return: Prints each log entry individually
        """
        for n in self.km_get_full_loglist():
            print(n)

    def start(self):
        """
        Main Kegging Process start method
        :return: starts the Kegging Process
        """
        try:
            print("Welcome to the Kegging Process")
            # batch_id = input("Please enter the batch id of the brite beer: ")
            self.brite_start()
            self.qa_start("Default Taster,", 0000, self.recipe_ibu)
            self.kt_start()
            self.kc_start()
            self.print_km_full_loglist()
        except Exception as e:
            print("Kegging Process Error: " + str(e))

# keg1 = KeggingMain(1234, "KEGGING_START_TEST", 38.5)
# keg1.start()
