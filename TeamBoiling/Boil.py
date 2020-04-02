# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Alex Hirsh (ajh6196@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed:
# Rev 1

import datetime
import time
import TeamBoiling.QualityCheck


class Boil():

    _boil_time = time
    _boil_temp = 0.0
    _stage_date_time = datetime
    _stage_duration = datetime
    _end_stage_date_time = datetime
    _is_boiling = bool


    def __init__(self):
        self._boil_time
        self._boil_temp
        self._stage_date_time
        self._stage_duration = datetime.datetime
        self._is_boiling

    def __init__(self, _boil_time, _boil_temp, _is_boiling):
        self._boil_time = _boil_time
        self._boil_temp = _boil_temp
        self._stage_date_time = datetime.datetime.now()
        self._stage_duration = datetime
        self._is_boiling = _is_boiling

    def get_boil_time(self):
        return self._boil_time
    def set_boil_time(self, _boil_time):
        self._boil_time = _boil_time

    def get_boil_temp(self):
        return self._boil_temp
    def set_boil_temp(self, _boil_temp):
        self._boil_temp = _boil_temp

    def get_stage_date_time(self):
        return self._stage_date_time
    def set_stage_date_time(self, _stage_date_time):
        self._stage_date_time = _stage_date_time

    def get_stage_duration(self):
        return self._stage_duration
    def set_stage_duration(self, _stage_duration):
        self._stage_duration = _stage_duration

    def start_boil(self):
        print("Start time: " + self._stage_date_time)
        print("Boil time (mins): " + self._boil_time)
        print("Boil temp: " + self._boil_temp)
        print("Is it boiling? : " + self._is_boiling)
        time.sleep(self._boil_time)
        qaCheck = TeamBoiling.QualityCheck()
        self.finish_boil(self, qaCheck)

    def finish_boil(self, qaCheck):
        print("QA Status: " + qaCheck)
        self._end_stage_date_time = datetime.datetime.now()
        print("End time: " + self._end_stage_date_time)
        duration = self._end_stage_date_time - self._stage_date_time
        self._stage_duration = duration.total_seconds()
        print("Boil stage duration (mins): " + self._stage_duration)
        print("Ending boil")

    def update_boil_status(self, _is_boiling):
        self._is_boiling = _is_boiling


