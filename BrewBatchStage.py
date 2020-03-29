# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Alex Hirsh (ajh6196@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed:
# Rev 1

import datetime
import time


class BrewBatchStage():

    _bb_stage_id = 0
    _bb_stage_start_date_time = datetime
    _bb_stage_end_date_time = datetime
    _bb_stage_duration = time
    _bb_stage_status = ""

    # constructor
    def __init__(self):
        self._bb_stage_id
        self._bb_stage_start_date_time
        self._bb_stage_end_date_time
        self._bb_stage_duration
        self._bb_stage_status

    def __init(self, _bb_stage_id, _bb_stage_start_date_time, _bb_stage_end_date_time, _bb_stage_duration, _bb_stage_status):
        self._bb_stage_id = _bb_stage_id
        self._bb_stage_start_date_time = datetime
        self._bb_stage_end_date_time = datetime
        self._bb_stage_duration = time
        self._bb_stage_status = _bb_stage_status

    # stage ID getters and setters
    def get_bb_stage_id(self):
        return self._bb_stage_id
    def set_bb_stage_id(self, _bb_stage_id):
        self._bb_stage_id = _bb_stage_id

    # stage start date and time getters and setters
    def get_bb_stage_start_date_time(self):
        return self._bb_stage_start_date_time
    def set_bb_stage_start_date_time(self, _bb_stage_start_date_time):
        self._bb_stage_start_date_time = _bb_stage_start_date_time

    # stage end date and time getters and setters
    def get_bb_stage_end_date_time(self):
        return self._bb_stage_end_date_time
    def set_bb_stage_end_date_time(self, _bb_stage_end_date_time):
        self._bb_stage_end_date_time = _bb_stage_end_date_time

    # stage duration getters and setters
    def get_bb_stage_duration(self):
        return self._bb_stage_duration
    def set_bb_stage_duration(self, _bb_stage_duration):
        self._bb_stage_duration = _bb_stage_duration

    # stage status getters and setters
    def get_bb_stage_status(self):
        return self._bb_stage_status
    def set_bb_stage_status(self, _bb_stage_status):
        self._bb_stage_status = _bb_stage_status
