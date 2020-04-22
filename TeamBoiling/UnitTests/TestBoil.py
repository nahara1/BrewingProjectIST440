# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for testing methods in Boil.py
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/1/2020
# Last Date Changed: 4/22/20
# Rev 5

import unittest
from TeamBoiling.Boil import Boil
from TeamBoiling.RecipeBoil import RecipeBoil


class TestBoil(unittest.TestCase):

    def test_boil_temp(self):
        b = Boil('request_number', 0, 'boil_time')
        r = RecipeBoil()
        self.assertEqual(b._boil_temp, r.boil_temp)

    def test_boil_time(self):
        b = Boil(0, 'boil_temp', 'request_number')
        r = RecipeBoil()
        self.assertEqual(b._boil_time, r.boil_time)

    def test_is_boiling(self):
        b = Boil('request_number', 'boil_temp', False)
        r = RecipeBoil()
        self.assertEqual(b._is_boiling, r.is_boiling)

