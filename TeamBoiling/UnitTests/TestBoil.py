# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Teresa Barker (tlb5767@psu.edu), Alex Hirsh (ajh6196@psu.edu)
# Date Developed: 4/1/2020
# Last Date Changed: 4/6/20
# Rev 3

import unittest
import TeamBoiling.Boil


class TestBoil(unittest.TestCase):

    # test start boil
    def test_start_boil(self):
        stage_date_time = TeamBoiling.Boil.Boil._stage_date_time
        self.assertEquals(stage_date_time, 0)

        boil_time = TeamBoiling.Boil.Boil._boil_time
        self.assertEquals(boil_time, 0)

        boil_temp = TeamBoiling.Boil.Boil._boil_temp
        self.assertEquals(boil_temp, 0)

        is_boiling = TeamBoiling.Boil.Boil._is_boiling
        self.assertEquals(is_boiling, True)

    # test finish boil
    def test_finish_boil(self):
        end_stage_date_time = TeamBoiling.Boil.Boil._end_stage_date_time
        self.assertEquals(end_stage_date_time, 0)

        stage_duration = TeamBoiling.Boil.Boil._stage_duration
        self.assertEquals(stage_duration, 0)

    # test update boil status
    def test_update_boil_status(self):
        is_boiling = TeamBoiling.Boil.Boil._is_boiling
        self.assertEquals(is_boiling, True)

    if __name__ == '__main__':
        unittest.main()
