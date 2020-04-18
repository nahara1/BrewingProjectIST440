# Project: Brewing Project
# Purpose Details: Main control for Kegging
# Course: IST 440W
# Author: Team Kegging
# Date Developed: 4/14/2020
# Last Date Changed: 4/14/2020
# Rev: 1.0

from TeamKegging.KeggingBriteTank import KeggingBriteTank
from TeamKegging.TasteTest import TasteTest
from Brewing.ServiceNowLog import ServiceNowLog
import datetime

full_loglist = []
def keg_log(batch_id, bb_stage, log_message):
    currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " +str(log_message) + "\"}"
    #ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
    print(status_log)


def brite_start():
    print("Welcome to the Kegging Process")
    batch_id = input("Please enter the batch id of the brite beer: ")

    bt1 = KeggingBriteTank(1,55,5,5,0,"BRITE_START")
    bt1.start_brite_tank(batch_id)
    full_loglist.extend(bt1.get_bt_loglist())

def qa_start():
    tt1 = TasteTest(1, "Daibo", 1111, "QA_START", 0)
    tt1.tt_main(1, 38.5)
    full_loglist.extend(tt1.get_tt_loglist())



brite_start()
qa_start()

for n in full_loglist:
    print(n)