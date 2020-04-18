# Project: Brewing Project
# Purpose Details: Main control for Kegging
# Course: IST 440W
# Author: Team Kegging
# Date Developed: 4/14/2020
# Last Date Changed: 4/14/2020
# Rev: 1.0

from TeamKegging.KeggingBriteTank import KeggingBriteTank
from Brewing.ServiceNowLog import ServiceNowLog
import datetime

def keg_log(batch_id, bb_stage, log_message):
    currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " +str(log_message) + "\"}"
    #ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
    print(status_log)

def brite_start():
    print("Welcome to the Kegging Process")
    batch_id = input("Please enter the batch id of the brite beer: ")

    bt1 = KeggingBriteTank(1,55,5,5,0,"BRITE_START")
    bt1.print_carb_status()
    bt1.start_brite_tank(1)
    qa_start()

def qa_start():
    print("this is a placeholder for taste test")


brite_start()