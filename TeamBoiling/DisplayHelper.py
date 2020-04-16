# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Erik Ellis (eae5206@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 4/15/2020
# Rev 2

import logging
from datetime import datetime
from time import sleep
from Brewing import UpdateLog


class DisplayHelper():

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

    def print_start_info(self, stage_date_time, boil_time, boil_temp, is_boiling):
        """
        Prints start stage information to the screen
        :param stage_date_time: Start time of the stage
        :param boil_time: Time boil lasts
        :param boil_temp: Temperature
        :param is_boiling: Is it boiling
        """
        print("Starting Boil Stage")
        sleep(1)
        print("Logging to ServiceNow...")
        sleep(1)
        status_log = "{\"boiling_stage\":\"Started Boiling\"}"
        UpdateLog.UpdateLog.log_to_service_now(self, status_log)
        print("Successfully logged that Boil Stage has started")
        print("-----------------------------------------")
        sleep(1)
        print("Start Time:", stage_date_time)
        sleep(1)
        print("Boil Time:", boil_time, "Minutes")
        sleep(1)
        print("Boil Temp:", boil_temp, "Degrees Celsius")
        print("-----------------------------------------")
        sleep(1)
        print("Turning on Burner...")
        sleep(3)
        print("Burner is up to temp! Temperature =", boil_temp, "degrees")
        sleep(1)
        print('Now boiling for', boil_time, "Minutes...")

    def print_end_info(self, end_stage_date_time, stage_duration):
        """
        Prints end stage information to the screen
        :param end_stage_date_time:  Time that the boil ends
        :param stage_duration:  Amount of time the stage lasted for
        """
        print("-----------------------------------------")
        print("Brew has finished boiling!")
        sleep(1)
        print("End time:", end_stage_date_time)
        sleep(1)
        print("Brew Boiled for", stage_duration, "minutes")
        print("-----------------------------------------")
        sleep(1)

    logging.info("Thread %s: finishing Getters and Setters")  # Threading


DisplayHelper = DisplayHelper('_boil_start_time', '_boil_time','_boil_temp', '_is_boiling')
