# Project: Brewing Automation System - Capstone Project
# Purpose Details: Class to initialize Brew Stage and Brew Batch
# Course: IST 440W - 001
# Author: Nahara (nkm5334)
# Date Developed: 4/18/20
# Last Date Changed: 4/18/20
# Rev 1

"""This module is used to initialize a new batch for the automated process to begin """

from Brewing import BrewBatch
from Brewing import BrewBatchStage
from Brewing.ServiceNowLog import ServiceNowLog
import datetime
from Brewing import Log
import time


def set_up_brew_stage(request_number):
    """
    Initializes a Brew Batch Stage Object in order to start the brewing process
    :param request_number: ServiceNow generated request number
    :return: a Brew Batch Stage object
    """
    print("Starting Prep Stage")

    # Create Prep BB Stage obj
    bbs = BrewBatchStage.BrewBatchStage(datetime.datetime.now(), 0, 'Recipe retrieved')

    time.sleep(1)
    # Create log in ServiceNow
    print("Logging to ServiceNow...")
    time.sleep(1)
    status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Starting Prep Process\"}"
    sn_log = ServiceNowLog()
    ServiceNowLog.create_new_log(sn_log, status_log)
    print("Successfully logged that Prep Stage has started")

    # Create local log
    log = Log.Log(12, "Prep", "Recipe Retrieved", datetime.datetime.now(), "pass")

    print("-----------------------------------------")
    print(log.generate_log())

    print("-----------------------------------------")
    return bbs


def start_brew_batch(request_number, brew_stage, recipe):
    """
    Starts a brew batch by setting up the brew batch id, initial stage, and corresponding recipe
    :param request_number: Request Number to be used as the Brew Batch ID
    :param brew_stage: Brew Batch Stage object
    :param recipe: Recipe Object
    :return:      a Brew Batch object
    """

    # Create log in ServiceNow
    print("Prep Stage in progress...")
    time.sleep(1)
    print("Logging to ServiceNow...")
    time.sleep(1)
    status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"Recipe has been retrieved\"}"
    ServiceNowLog.ServiceNowLog.create_new_log(status_log)
    print("Successfully logged that Prep Stage is in progress")

    print("-----------------------------------------")
    log = Log.Log("Prep", "Prep Initialized", datetime.datetime.now(), "pass")
    print(log.generate_log())
    print("-----------------------------------------")

    # Save log to MongoDB

    # Create a BrewBatch object to be returned and passed along to the other brew phases
    brew_batch = BrewBatch.BrewBatch(request_number, recipe, datetime.datetime.now(),
                                     brew_stage,
                                     "Prep Stage",
                                     recipe.get_batch_size())

    return brew_batch
