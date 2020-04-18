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
    #ServiceNowLog.ServiceNowLog.create_new_log(ServiceNowLog, status_log)
    print(status_log)



def temp_start(batch_id,KeggingBriteTank):
    KeggingBriteTank.temp_choice()
    log_message = "Brite Tank Temperature in Range"
    keg_log(batch_id, "Kegging", log_message)

def psi_start(batch_id,KeggingBriteTank):
    KeggingBriteTank.psi_choice()
    log_message = "Brite Tank Pressure in Range"
    keg_log(batch_id, "Kegging", log_message)

def carb_start(batch_id,KeggingBriteTank):
    recipe_carb = float(input("Please enter the target carbonation volume: "))
    KeggingBriteTank.auto_carb(recipe_carb,1)
    log_message = "Carbonation Ready at " + str(KeggingBriteTank.get_carbonation()) + " volumes"
    keg_log(batch_id,"Kegging", log_message)

def brite_start():
    print("Welcome to the Kegging Process")
    batch_id = input("Please enter the batch id of the brite beer: ")

    bt1 = KeggingBriteTank(1,55,5,5,0,"BRITE_START")
    bt1.print_carb_status()
    temp_start(batch_id,bt1)
    psi_start(batch_id,bt1)
    carb_start(batch_id,bt1)
    print("Batch is ready for Taste Test QA")
    keg_log(batch_id,"Kegging","Preparing for Taste Test QA")
    ttqa_start()

def ttqa_start()
    print("this is a placeholder for taste test")


brite_start()