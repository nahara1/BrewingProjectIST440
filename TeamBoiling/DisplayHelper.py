# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for creating command line displays
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 3/18/20
# Last Date Changed: 4/23/2020
# Rev 5

import sys
import logging
from datetime import datetime
from time import sleep
from Brewing.ServiceNowLog import ServiceNowLog
from Brewing import MongoLogging

sleep_time = .75


class DisplayHelper:

    _boil_start_time = datetime
    _boil_time = float
    _boil_temp = float
    _is_boiling = bool

    def __init__(self, boil_start_time, boil_time, boil_temp, is_boiling):
        self._boil_start_time = boil_start_time
        self._boil_time = boil_time
        self._boil_temp = boil_temp
        self._is_boiling = is_boiling

    logging.info("Thread %s: starting Getters and Setters")  # Threading

    def print_start_info(self, request_number, boil_temp, boil_time, stage_date_time):
        """
        Prints start stage information to the screen
        :param request_number:
        :param stage_date_time: Start time of the stage
        :param boil_time: Time boil lasts
        :param boil_temp: Temperature
        :param is_boiling: Is it boiling
        """
        print("Starting Boil Stage")
        sleep(sleep_time)
        print("Logging to ServiceNow...")
        sleep(sleep_time)
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Boiling\", \"log\":\"Starting Boil Process\"}"
        sn_log = ServiceNowLog()
        ServiceNowLog.create_new_log(sn_log, status_log)
        sleep(sleep_time)
        print("Logging to MongoDB...")
        sleep(sleep_time)
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Boiling", "Starting Boil Process")
        print("Successfully logged that Boil Stage has started")
        print("-----------------------------------------")
        sleep(sleep_time)
        print("Start Time:", stage_date_time)
        sleep(sleep_time)
        print("Boil Time:", boil_time, "Minutes")
        sleep(sleep_time)
        print("Boil Temp:", boil_temp, "Degrees Celsius")
        print("-----------------------------------------")
        sleep(sleep_time)
        print("Turning on Burner...")
        sleep(sleep_time*3)
        print("Burner is up to temp! Temperature =", boil_temp, "degrees")
        sleep(sleep_time)
        print('Now boiling for', boil_time, "Minutes...")

    def print_end_info(self, end_stage_date_time, stage_duration):
        """
        Prints end stage information to the screen
        :param end_stage_date_time:  Time that the boil ends
        :param stage_duration:  Amount of time the stage lasted for
        """
        print("-----------------------------------------")
        print("End time:", end_stage_date_time)
        sleep(sleep_time)
        print("-----------------------------------------")
        sleep(sleep_time)

    logging.info("Thread %s: finishing Getters and Setters")  # Threading


DisplayHelper = DisplayHelper('_boil_start_time', '_boil_time','_boil_temp', '_is_boiling')
