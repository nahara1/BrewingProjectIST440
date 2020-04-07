# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Erik Ellis (eae5206@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 3/31/20
# Rev 1

import datetime
import time
import logging
from TeamBoiling import BrewBatchStage


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
        '''
        Constructor Method for Brew Batch
        '''
        self._bb_id
        self._recipe_id
        self._bb_start_date_time = datetime.datetime.utcnow()
        self._bb_end_date_time = datetime.datetime.utcnow()
        self._bb_stage
        self._bb_duration
        self._bb_status
        self._bb_size

    def __init__(self, recipe_id, bb_start_date_time, bb_end_date_time, bb_stage, bb_status, bb_size):
        '''
        Overloaded Constructor Method allows parameters to be accessed with methods and attributes
        :param recipe_id: ID for the recipe of the brew batch
        :param bb_start_date_time:  start date and time of the brew batch
        :param bb_end_date_time: end date and time of the brew batch
        :param bb_stage: stage of the brew batch
        :param bb_status: the brew batch's status
        :param bb_size: size of the brew batch
        '''
        logging.info("Thread %s: starting BrewBatch", self)  # Threading
        ++self._bb_id
        self._recipe_id = recipe_id
        self._bb_start_date_time = bb_start_date_time
        self._bb_end_date_time = bb_end_date_time
        self._bb_duration = bb_end_date_time - bb_start_date_time
        self._bb_status = bb_status
        self._bb_size = bb_size
        logging.info("Thread %s: finishing BrewBatch", self)  # Threading

    logging.info("Thread %s: starting Getters and Setters")  # Threading

    def get_brew_batch_id(self):
        '''
        Gets the Brew Batch's ID
        :return: returns the ID of the brew batch to be set
        '''
        return self._bb_id

    def set_brew_batch_id(self, bb_id):
        '''
        Setter for brew batch ID,
        :param bb_id: sets the id for the brew batch
        :return: returns the ID for the brew batch
        '''
        self._bb_id = bb_id

    def get_recipe_id(self):
        '''
        Calls the Recipe ID to be set for the recipe
        :param self: allows access to the recipe ID
        :return: returns the recipe id
        '''
        return self._recipe_id

    def set_recipe_id(self, recipe_id):
        '''
        Setter for the recipe's ID
        :param self: sets the recipe ID
        :param recipe_id: Variable for the recipe ID to be set
        :return: returns the recipe ID to be set
        '''
        self._recipe_id = recipe_id

    def get_bb_start_date_time(self):
        '''
        Gets the Brew batch start date and time
        :param self: calls the start date and time of the brew batch
        :return: returns the start date and time
        '''
        return self._bb_start_date_time

    def set_bb_start_date_time(self, bb_start_date_time):
        '''
        Setter for the start date and time of the brew batch
        :param self: calls the start date and time
        :param bb_start_date_time: start date and time for brew batch
        :return: returns the start date and time, setting it for brew batch
        '''
        self._bb_start_date_time = bb_start_date_time

    def get_bb_end_date_time(self):
        '''
        gets the end date and time for brew batch
        :param self: calls the end date and time
        :return: returns the end date and time for brew batch
        '''
        return self._bb_end_date_time

    def set_bb_end_date_time(self, bb_end_date_time):
        '''
        setter for end date and time of brew batch
        :param self: calls the end date and time
        :param bb_end_date_time: end date and time for brew batch
        :return: returns and sets end date and time for brew batch
        '''
        self._bb_end_date_time = bb_end_date_time

    def get_bb_stage(self):
        '''
        Gets the stage of the brew batch
        :return: returns the stage
        '''
        return self

    def set_bb_stage(self, bb_stage):
        '''
        sets the stage for brew batch
        :param bb_stage: brew batch stage
        :return: returns and sets the brew batch stage
        '''
        self._bb_stage = bb_stage

    def get_bb_duration(self):
        '''
        Calls the duration of the brew batch
        :return: returns the duration time
        '''
        return self._bb_duration

    def set_bb_duration(self, bb_duration):
        '''
        sets the duration time of the brew batch
        :param bb_duration: time of the brew batch duration
        :return: returns duration time and sets it
        '''
        self._bb_duration = bb_duration

    def get_bb_status(self):
        '''
        Gets the status of the brew batch
        :return: returns the status of the brew batch
        '''
        return self._bb_status

    def set_bb_status(self, bb_status):
        '''
        Sets the status for Brew batch
        :param bb_status: brew batch status
        :return: returns and sets the status of brew batch
        '''
        self._bb_status = bb_status

    def get_bb_size(self):
        '''
        Gets the size of the brew batch
        :return: returns brew batch size
        '''
        return self._bb_size

    def set_bb_size(self, bb_size):
        '''
        Sets the size of the brew batch
        :param bb_size: size of the brew batch
        :return: returns and sets the size of the brew batch
        '''
        self._bb_size = bb_size

    logging.info("Thread %s: finishing Getters and Setters")  # Threading