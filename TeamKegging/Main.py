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

full_loglist = []
def keg_log(batch_id, bb_stage, log_message):
    currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " +str(log_message) + "\"}"
    #ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
    print(status_log)


def brite_start(batch_id):

    bt1 = KeggingBriteTank(1,55,5,5,0,"BRITE_START")
    bt1.start_brite_tank(batch_id)
    full_loglist.extend(bt1.get_bt_loglist())

def qa_start(batch_id):
    tt1 = TasteTest(batch_id, "Daibo", 1111, "QA_START", 0)
    tt1.tt_main(1, 38.5)
    full_loglist.extend(tt1.get_tt_loglist())

def kt_start():
    kt1 = KeggingTasks(1, 'Cellarman tasks', 'TASK_START')
    kt1.Keggingtasksmain()
    full_loglist.extend((kt1.get_kt_loglist()))

def main():
    print("Welcome to the Kegging Process")
    batch_id = input("Please enter the batch id of the brite beer: ")
    brite_start(batch_id)
    qa_start(batch_id)
    kt_start()

    for n in full_loglist:
        print(n)

main()
