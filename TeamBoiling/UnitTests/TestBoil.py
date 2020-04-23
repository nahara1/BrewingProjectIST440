# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for testing methods in Boil.py
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/1/2020
# Last Date Changed: 4/16/20
# Rev 4

import unittest
from TeamBoiling.Boil import QualityCheck
from TeamBoiling.Boil import Boil
from TeamBoiling.UnitTests import TempBoilRecipe
from Brewing import Recipe


class TestBoil(unittest.TestCase):

    # test start boil
    def test_print_start_boil(self):
        test_boil_time = QualityCheck.QualityCheck.print_start_info.boil_time
        self.assertEquals(test_boil_time, 10)

    def test_boil_time(self):
        b = Boil.get_boil_time()
        br = TempBoilRecipe.TempBoilRecipe()
        # br = Recipe.Recipe()      waiting for recipe class to populate
        self.assertEqual(b._boil_time, br.boil_time)
        
    def test_start_boil(self):
        stage_date_time = Boil._stage_date_time
        self.assertEquals(stage_date_time, 0)

        boil_time = Boil._boil_time
        self.assertEquals(boil_time, 0)

        boil_temp = Boil._boil_temp
        self.assertEquals(boil_temp, 0)

        is_boiling = Boil._is_boiling
        self.assertEquals(is_boiling, True)

    # test finish boil
    def test_finish_boil(self):
        end_stage_date_time = Boil._end_stage_date_time
        self.assertEquals(end_stage_date_time, 0)

        stage_duration = Boil._stage_duration
        self.assertEquals(stage_duration, 0)

    # test update boil status
    def test_update_boil_status(self):
        is_boiling = Boil._is_boiling
        self.assertEquals(is_boiling, True)

    if __name__ == '__main__':
        unittest.main()
