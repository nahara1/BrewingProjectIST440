# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for implementing quality assurance
# Course: IST 440W - 001
# Author: Teresa Barker (tlb5767@psu.edu), Alex Hirsh (ajh6196@psu.edu), David Karminski (dck5200@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 4/16/2020
# Rev 10

# Import Statements
import time
import logging
from Brewing import ServiceNowLog
from time import sleep


class QualityCheck:

    # Variables
    _recipe_boil_temp = float
    _batch_boil_time = time
    _recipe_boil_time = time
    _batch_boil_temp = float
    _boil_over = bool
    _overflowing = bool
    _correct_volume = bool

    def __init__(self, _recipe_boil_temp, _batch_boil_time, _batch_boil_temp, _recipe_boil_time, _boil_over, _overflowing, _correct_volume):
        """
        Constructor method and parameters initialized to be accessed
        :param _recipe_boil_temp: Boil temperature of the recipe
        :param _batch_boil_time: boil time of the batch
        :param _batch_boil_temp: boil temperature of the batch
        :param _recipe_boil_time: boil time of the recipe
        :param _boil_over: mixture boiling over
        :param _overflowing: mixture overflowing
        :param _correct_volume: validates volume of the batch
        """
        logging.info("Thread %s: starting QACheck", self)  # Threading
        self._recipe_boil_temp = _recipe_boil_temp
        self._batch_boil_time = _batch_boil_time
        self._recipe_boil_time = _recipe_boil_time
        self._batch_boil_temp = _batch_boil_temp
        self._boil_over = _boil_over
        self._overflowing = _overflowing
        self._correct_volume = _correct_volume
        logging.info("Thread %s: finishing QACheck", self)  # Threading

    # Getters and Setters
    # Recipe Boil Temp
    logging.info("Thread %s: starting Getters and Setters")  # Threading

    def get_recipe_boil_temp(self):
        """
        Calls the recipe boil temperature
        :return: returns the boiling temperature of the mixture
        """
        return self._recipe_boil_temp

    def set_recipe_boil_temp(self, _recipe_boil_temp):
        """
        Setter for the boil temperature
        :param _recipe_boil_temp: boiling temperature
        :return: returns and sets the boiling temperature
        """
        self._recipe_boil_temp = _recipe_boil_temp

    # Batch Boil Time
    def get__batch_boil_time(self):
        """
        Calls the batch boiling time
        :return: returns the boiling time for the batch
        """
        return self._batch_boil_time

    def set__batch_boil_time(self, _batch_boil_time):
        """
        Sets the batch boiling time
        :param _batch_boil_time: boiling time of the batch
        :return: returns and sets the batch boiling time
        """
        self._batch_boil_time = _batch_boil_time

    # Recipe Boil Time
    def get__recipe_boil_time(self):
        """
        Calls the recipe boiling time
        :return: returns boiling time of the recipe
        """
        return self._recipe_boil_time

    def set_recipe_boil_time(self, _recipe_boil_time):
        """
        Setter for boiling time of the recipe
        :param _recipe_boil_time:  recipe boiling time
        :return: returns and sets the recipe time to be boiled at
        """
        self._recipe_boil_time = _recipe_boil_time

    # Batch Boil Temp
    def get_batch_boil_temp(self):
        """
        Calls the boiling temperature of the batch
        :return: returns the boiling temperature of the batch
        """
        return self._batch_boil_temp

    def set_batch_boil_temp(self, _batch_boil_temp):
        """
        Setter for the batch boiling temperature
        :param _batch_boil_temp: temperature for the boiling of the batch
        :return: returns the batch boiling temperature and sets it for the batch
        """
        self._batch_boil_temp = _batch_boil_temp

    # Boil Over
    def get_boil_over(self):
        """
        Calls to see if the batch boiled over
        :return: returns boil over status
        """
        return self._boil_over

    def set_boil_over(self, _boil_over):
        """
        Setter for boil over
        :param _boil_over: boil over variable
        :return: returns the boil over status and sets it to validate if it's boiled over
        """
        self._boil_over = _boil_over

    # Overflowing
    def get_overflowing(self):
        """
        Calls the batch to see if it's overflowing
        :return: returns the overflowing status
        """
        return self._overflowing

    def set_overflowing(self, _overflowing):
        """
        Setter for overflowing
        :param _overflowing: validates to see if the batch is overflowing
        :return: returns the overflowing status and sets it
        """
        self._overflowing = _overflowing

    # Correct Volume
    def get_correct_volume(self):
        """
        Gets the correct volume for the recipe
        :return: returns the correct volume of the recipe
        """
        return self._correct_volume

    def set_correct_volume(self, _correct_volume):
        """
        Setter for the correct volume
        :param _correct_volume: correct volume of the recipe
        :return: returns the correct volume and sets it for the recipe
        """
        self._correct_volume = _correct_volume

    logging.info("Thread %s: finishing Getters and Setters")  # Threading


    def get_QA_Check(self):
        text = input("Please Inspect the Brew Quality. Does it Meet Our Standards (Yes/No)?: ")
        # save text as variable
        quality_checked = text
        while quality_checked != "Yes" or quality_checked != "No":
            if quality_checked == "Yes":
                print("Logging to ServiceNow...")
                sleep(1)
                status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Boiling\", \"log\":\"Finished Boiling; Passed QA\"}"
                ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
                sleep(1)
                print("Successfully logged that Boil has completed and passes Quality Assurance.")
                sleep(1)
                # Call Team Ferment
                break
            elif quality_checked == "No":
                print("Logging to ServiceNow...")
                sleep(1)
                status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Boiling\", \"log\":\"Finished Boiling; Failed QA\"}"
                ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
                sleep(1)
                print("Quality Did not Pass, Please inspect and trash.")
                sleep(1)
                break
            else:
                text = input("Please Enter Yes or No: ")
                quality_checked = text


QualityCheck = QualityCheck('_recipe_boil_temp', '_batch_boil_time', '_batch_boil_temp', '_recipe_boil_time',
                            '_boil_over', '_overflowing', '_correct_volume')
# QualityCheck.get_QA_Check()
