# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Alex Hirsh (ajh6196@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 4/6/2020
# Rev 2


import datetime
import time
import logging


class BrewBatchStage():

    _bb_stage_id = 0
    _bb_stage_start_date_time = datetime
    _bb_stage_end_date_time = datetime
    _bb_stage_duration = time
    _bb_stage_status = ""

    # constructor
    def __init__(self):
        """
        constructor method for BrewBatchStage
        :param self: allows access to attributes and methods
        """
        self._bb_stage_id
        self._bb_stage_start_date_time
        self._bb_stage_end_date_time
        self._bb_stage_duration
        self._bb_stage_status

    def __init__(self, _bb_stage_id, _bb_stage_start_date_time, _bb_stage_end_date_time, _bb_stage_duration, _bb_stage_status):
        """
        Overloads constructor with parameters
        :param _bb_stage_id: ID for BrewBatchStage
        :param _bb_stage_start_date_time: Start Date and time for the stage of brew batch
        :param _bb_stage_end_date_time: End Date and time for the stage of brew batch
        :param _bb_stage_duration: duration of the brew batch stage
        :param _bb_stage_status: status of the brew batch stage
        """

        logging.info("Thread %s: Brew Batch Starting", self)
        self._bb_stage_id = _bb_stage_id
        self._bb_stage_start_date_time = datetime
        self._bb_stage_end_date_time = datetime
        self._bb_stage_duration = time
        self._bb_stage_status = _bb_stage_status
        logging.info("Thread %s: Brew Batch Ending", self)

    # stage ID getters and setters
    logging.info("Thread %s: Start Getters and Setters")

    def get_bb_stage_id(self):
        """
        Gets the Brew Batch's Stage ID
        :return:  returns the Stage Id for that brew batch
        """
        return self._bb_stage_id

    def set_bb_stage_id(self, _bb_stage_id):
        """
        Setter for the Stage Id of the Brew Batch
        :param _bb_stage_id: sets the stage id for brew batch
        :return: returns the brew batch stage id
        """
        self._bb_stage_id = _bb_stage_id

    # stage start date and time getters and setters
    def get_bb_stage_start_date_time(self):
        """
        Gets the stage start date and time of the brew batch
        :return: returns brew batch stage start date and time
        """
        return self._bb_stage_start_date_time

    def set_bb_stage_start_date_time(self, _bb_stage_start_date_time):
        """
        Setter for the stage start date and time
        :param _bb_stage_start_date_time: sets the start date and time
        :return: returns the stage start date and time for brew batch
        """
        self._bb_stage_start_date_time = _bb_stage_start_date_time

    # stage end date and time getters and setters
    def get_bb_stage_end_date_time(self):
        """
        Gets the brew batch stage end date and time
        :return: returns brew batch stage end date and time
        """
        return self._bb_stage_end_date_time

    def set_bb_stage_end_date_time(self, _bb_stage_end_date_time):
        """
        Setter for stage end date and time of brew batch
        :param _bb_stage_end_date_time: end date and time for stage of brew batch
        :return: returns stage end date and time
        """
        self._bb_stage_end_date_time = _bb_stage_end_date_time

    # stage duration getters and setters
    def get_bb_stage_duration(self):
        """
        Gets stage duration for brew batch
        :return: returns duration time for current stage of brew batch
        """
        return self._bb_stage_duration

    def set_bb_stage_duration(self, _bb_stage_duration):
        """
        Setter for duration of the time stage of brew batch
        :param _bb_stage_duration: time spent during stage of brew batch
        :return: returns brew batch stage duration
        """
        self._bb_stage_duration = _bb_stage_duration

    logging.info("Thread %s: End Getters and Setters")

