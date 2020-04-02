# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Erik Ellis (eae5206@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed:
# Rev 1

import datetime
import time
import BrewBatchStage

class BrewBatch():

    _bb_id = 0
    _recipe_id = 0
    _bb_start_date_time = datetime
    _bb_end_date_time = datetime
    _bb_stage = BrewBatchStage
    _bb_duration = time
    _bb_status = ""
    _bb_size = ""

    def __init__(self):
        self._bb_id
        self._recipe_id
        self._bb_start_date_time = datetime.datetime.utcnow()
        self._bb_end_date_time = datetime.datetime.utcnow()
        #self._bb_stage
        self._bb_duration
        self._bb_status
        self._bb_size

    def __init__(self, recipe_id, bb_start_date_time, bb_end_date_time, bb_stage, bb_status, bb_size):
        ++self._bb_id
        self._recipe_id = recipe_id
        self._bb_start_date_time = bb_start_date_time
        self._bb_end_date_time = bb_end_date_time
        self._bb_duration = bb_end_date_time - bb_start_date_time
        self._bb_stage = bb_stage
        self._bb_status = bb_status
        self._bb_size = bb_size

    def get_brew_batch_id(self):
        return self._bb_id

    def set_brew_batch_id(self, bb_id):
         self._bb_id = bb_id

    def get_recipe_id(self):
        return self._recipe_id

    def set_recipe_id(self, recipe_id):
        self._recipe_id = recipe_id

    def get_bb_start_date_time(self):
        return self._bb_start_date_time

    def set_bb_start_date_time(self, bb_start_date_time):
        self._bb_start_date_time = bb_start_date_time

    def get_bb_end_date_time(self):
        return self._bb_end_date_time

    def set_bb_end_date_time(self, bb_end_date_time):
        self._bb_end_date_time = bb_end_date_time

    def get_bb_stage(self):
        return self

    def set_bb_stage(self, bb_stage):
        self._bb_stage = bb_stage

    def get_bb_duration(self):
        return self._bb_duration

    def set_bb_duration(self, bb_duration):
        self._bb_duration = bb_duration

    def get_bb_status(self):
        return self._bb_status

    def set_bb_status(self, bb_status):
        self._bb_status = bb_status

    def get_bb_size(self):
        return self._bb_size

    def set_bb_size(self, bb_size):
        self._bb_size = bb_size
