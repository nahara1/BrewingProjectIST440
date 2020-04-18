# Project: Brewing Project
# Purpose Details: Main control for Kegging
# Course: IST 440W
# Author: Team Kegging
# Date Developed: 4/14/2020
# Last Date Changed: 4/14/2020
# Rev: 1.0

from TeamKegging.KeggingBriteTank import KeggingBriteTank
from TeamKegging.TasteTest import TasteTest
from TeamKegging.KeggingTasks import KeggingTasks
from Brewing.ServiceNowLog import ServiceNowLog
import datetime

km_full_loglist = []


class KeggingMain:
    def __init__(self, batch_id, kegging_status):
        self.batch_id = batch_id
        self.kegging_status = kegging_status

    def keg_log(self, bb_stage, log_message):
        currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        status_log = "{\"batch_id\":\"" + str(self.batch_id) + "\", \"brew_batch_stage\":\"" + str(
            bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " + str(log_message) + "\"}"
        # ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        print(status_log)

    def brite_start(self):
        bt1 = KeggingBriteTank(1, 55, 5, 5, 0, "BRITE_START")
        bt1.start_brite_tank(self.batch_id)
        km_full_loglist.extend(bt1.get_bt_loglist())

    def qa_start(self):
        tt1 = TasteTest(self.batch_id, "Daibo", 1111, "QA_START", 0)
        tt1.tt_main(1, 38.5)
        km_full_loglist.extend(tt1.get_tt_loglist())

    def kt_start(self):
        kt1 = KeggingTasks(self.batch_id, 'Cellarman tasks', 'TASK_START')
        kt1.Keggingtasksmain()
        km_full_loglist.extend((kt1.get_kt_loglist()))

    def km_get_full_loglist(self):
        return km_full_loglist

    def print_km_full_loglist(self):
        for n in self.km_get_full_loglist():
            print(n)

    def start(self):
        print("Welcome to the Kegging Process")
        batch_id = self.batch_id
        #batch_id = input("Please enter the batch id of the brite beer: ")
        self.brite_start()
        self.qa_start()
        self.kt_start()

keg1 = KeggingMain(1234,"KEGGING_START")
keg1.start()