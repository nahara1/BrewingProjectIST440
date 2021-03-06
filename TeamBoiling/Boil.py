# Project: Brewing Automation System - Capstone Project
# Purpose Details: Main class for Boil Process that runs helper classes
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 3/18/20
# Last Date Changed: 4/18/2020
# Rev 7

import datetime
import sys
import time
import logging

from TeamBoiling import QualityCheck
from TeamBoiling import DisplayHelper
from TeamBoiling import SensorHelper
from TeamBoiling.UnitTests import TempBoilRecipe


class Boil:

    _boil_time = time
    _boil_temp = 0.0
    _stage_date_time = datetime
    _stage_duration = datetime
    _end_stage_date_time = datetime
    _is_boiling = bool

    def __init__(self, _boil_time, _boil_temp, _is_boiling):
        """
        overloads constructor method for parameters
        :param _boil_time: boiling duration
        :param _boil_temp: boiling temperature
        :param _stage_date_time: timestamp for the stage
        :param _stage_duration: duration of time during boil stage
        :param _is_boiling: validates boiling
        """
        logging.info("Thread %s: Start Boiling", self)
        self._boil_time = TempBoilRecipe.TempBoilRecipe.boil_time
        self._boil_temp = TempBoilRecipe.TempBoilRecipe.boil_temp
        self._stage_date_time = datetime.datetime.now()
        self._stage_duration = datetime.datetime
        self._is_boiling = _is_boiling
        logging.info("Thread %s: End Boiling", self)

    logging.info("Thread %s: Start Getters and Setters")

    def get_boil_time(self):
        """
        gets the boiling time
        :return: boiling time
        """
        return self._boil_time

    def set_boil_time(self, _boil_time):
        """
        setter for boiling time
        :param _boil_time: sets the boil time
        :return: the boiling time after being set
        """
        self._boil_time = _boil_time

    def get_boil_temp(self):
        """
        Gets the boiling temperature
        :return: returns the boiling temperature
        """
        return self._boil_temp

    def set_boil_temp(self, _boil_temp):
        """
        Setter for boiling temperature
        :param _boil_temp: allows the temperature to be set
        :return: the boiling temperature
        """
        self._boil_temp = _boil_temp

    def get_stage_date_time(self):
        """
        gets the date and time of the boiling stage
        :return: returns the stage date and time
        """
        return self._stage_date_time

    def set_stage_date_time(self, _stage_date_time):
        """
        Setter for stage date and time
        :param _stage_date_time: timestamp of the stage
        :return: returns boiling stage date and time
        """
        self._stage_date_time = _stage_date_time

    def get_stage_duration(self):
        """
        Gets the stage duration
        :return: returns the time of the boiling stage
        """
        return self._stage_duration

    def set_stage_duration(self, _stage_duration):
        """
        Setter for the duration of the boiling stage
        :param _stage_duration: sets the duration of the boiling stage
        :return: boiling stage time
        """
        self._stage_duration = _stage_duration

    logging.info("Thread %s: End Getters and Setters")

    def start_boil(self):
        """
        Initiates the boiling process
        :return: start of boiling process
        """
        logging.info("Thread %s: Start Boiling", self)
        DisplayHelper.print_start_info(self._stage_date_time, self._boil_time, self._boil_temp, self._is_boiling)

    def update_boil_status(self, _is_boiling):
        """
        Updates boiling status from start to finish
        :param _is_boiling: checks that boiling is in progress
        :return: returns boiling status
        """
        self._is_boiling = _is_boiling
        logging.info("Thread %s: Update Boiling Status", self)

    def finish_boil(self, qaCheck):
        print("QA Status: " + qaCheck)
        self._end_stage_date_time = datetime.datetime.now()
        duration = self._end_stage_date_time - self._stage_date_time
        self._stage_duration = duration.total_seconds()
        DisplayHelper.print_end_info(self._end_stage_date_time, self._stage_duration)
        self.update_boil_status(False)
        logging.info("Thread %s: Stop Boiling", self)


# Method to run Boil Process from Main.py


def run_boil(request_number, boil_temp, boil_time):
    DisplayHelper.DisplayHelper.print_start_info(request_number, boil_temp, boil_time, stage_date_time=datetime.datetime.now())
    SensorHelper.SensorHelper.boil_timer(request_number, boil_time)
    DisplayHelper.DisplayHelper.print_end_info(end_stage_date_time=datetime.datetime.now(), stage_duration=boil_time)
    return QualityCheck.QualityCheck.get_QA_Check(request_number)

