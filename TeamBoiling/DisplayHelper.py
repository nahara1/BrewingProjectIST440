# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Erik Ellis (eae5206@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 4/12/2020
# Rev 1

import logging, time
from datetime import datetime


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
        print("Start time: " + stage_date_time)
        print("Boil time (mins): " + boil_time)
        print("Boil temp: " + boil_temp)
        print("Is it boiling? : " + is_boiling)
        print('Now boiling for ' + boil_time)
        #Boil.update_boil_status(False)

    def print_end_info(self, end_stage_date_time, stage_duration):
        """
        Prints end stage information to the screen
        :param end_stage_date_time:  Time that the boil ends
        :param stage_duration:  Amount of time the stage lasted for
        """
        print("End time: " + end_stage_date_time)
        print("Boil stage duration (mins): " + stage_duration)
        print("Ending boil")

    logging.info("Thread %s: finishing Getters and Setters")  # Threading


DisplayHelper = DisplayHelper('_boil_start_time', '_boil_time','_boil_temp', '_is_boiling')