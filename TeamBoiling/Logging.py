# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for controlling sensors
# Course: IST 440W - 001
# Author: Alex Hirsh(ajh6196@psu.edu)
# Date Developed: 3/31/2020
# Last Date Changed: 3/31/2020
# Rev 1


class Logging():
    _recipe_id = int
    _bb_id = int
    #_bb_stage = BBStage
    _recipe_status = str

    def __init__(self):
        """
        constructor method for logging class, initializes class.
        """
        self._recipe_id
        self._bb_id
        #self._bb_stage
        self._recipe_status

    def __init__(self, _recipe_id, _bb_id, _bb_stage, _recipe_status):
        """
        Overloads constructor method to access methods and attributes
        :param _recipe_id: ID for the recipe
        :param _bb_id: ID for the brew batch
        :param _bb_stage: Stage of the brew batch
        :param _recipe_status: Status of the recipe
        """
        self._recipe_id = _recipe_id
        self._bb_id = _bb_id
        #self._bb_stage = _bb_stage
        self._recipe_status = _recipe_status

    def add_recipe_id(self, _recipe_id):
        """
        Adds the recipe ID to the log of the order
        :param _recipe_id:
        :return: ID for Recipe
        """
        self._recipe_id = _recipe_id

    def add_bb_id(self, _bb_id):
        """
        Adds the Brew Batch ID to the order log
        :param _bb_id: brew batch ID
        :return: returns ID for brew batch to add to log
        """
        self._bb_id = _bb_id

    #def add_bb_stage(self, _bb_stage):
        #self._bb_stage = _bb_stage

    def add_recipe_status(self, _recipe_status):
        """
        Adds the Status of the recipe to the order log
        :param _recipe_status: calls the status of the recipe
        :return: returns the status of the recipe
        """
        self._recipe_status = _recipe_status