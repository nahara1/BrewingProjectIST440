# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for testing quality assurance
# Course: IST 440W - 001
# Author: Teresa Barker(tlb5767@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 3/18/2020
# Rev 1

# Import Statements
import time


class QualityCheck():

    # Variables
    _recipe_boil_temp = float
    _batch_boil_time = time
    _recipe_boil_time = time
    _batch_boil_temp = float
    _boil_over = bool
    _overflowing = bool
    _correct_volume = bool

    def __init__(self):
        self._recipe_boil_temp
        self._batch_boil_time
        self._recipe_boil_time
        self._batch_boil_temp
        self._boil_over
        self._overflowing
        self._correct_volume

    def __init__(self, _recipe_boil_temp, _batch_boil_time, _batch_boil_temp, _recipe_boil_time, _boil_over, _overflowing, _correct_volume):
        self._recipe_boil_temp = _recipe_boil_temp
        self._batch_boil_time = _batch_boil_time
        self._recipe_boil_time = _recipe_boil_time
        self._batch_boil_temp = _batch_boil_temp
        self._boil_over = _boil_over
        self._overflowing = _overflowing
        self._correct_volume = _correct_volume

    # Getters and Setters
    # Recipe Boil Temp
    def get_recipe_boil_temp(self):
        return self._recipe_boil_temp

    def set_recipe_boil_temp(self, _recipe_boil_temp):
        self._recipe_boil_temp = _recipe_boil_temp

    # Batch Boil Time
    def get__batch_boil_time(self):
        return self._batch_boil_time

    def set__batch_boil_time(self, _batch_boil_time):
        self._batch_boil_time = _batch_boil_time

    # Recipe Boil Time
    def get__recipe_boil_time(self):
        return self._recipe_boil_time

    def set_recipe_boil_time(self, _recipe_boil_time):
        self._recipe_boil_time = _recipe_boil_time

    # Batch Boil Temp
    def get_batch_boil_temp(self):
        return self._batch_boil_temp

    def set_batch_boil_temp(self, _batch_boil_temp):
        self._batch_boil_temp = _batch_boil_temp

    # Boil Over
    def get_boil_over(self):
        return self._boil_over

    def set_boil_over(self, _boil_over):
        self._boil_over = _boil_over

    # Overflowing
    def get_overflowing(self):
        return self._overflowing

    def set_overflowing(self, _overflowing):
        self._overflowing = _overflowing

    # Correct Volume
    def get_correct_volume(self):
        return self._correct_volume

    def set_correct_volume(self, _correct_volume):
        self._correct_volume = _correct_volume
