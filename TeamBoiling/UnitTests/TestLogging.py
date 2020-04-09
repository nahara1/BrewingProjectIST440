# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Alex Hirsh (ajh6196@psu.edu)
# Date Developed: 4/6/2020
# Last Date Changed: 4/6/2020
# Rev 1

import unittest
import TeamBoiling.Logging


class TestLogging(unittest.TestCase):
    def test_logging_add_recipe(self):
        recipe_ID = TeamBoiling.Logging.Logging.add_recipe_id
        self.assertEquals(recipe_ID, 0)

    def test_logging_add_bb(self):
        bb_id = TeamBoiling.Logging.Logging.add_bb_id
        self.assertEquals(bb_id, 0)

    def test_logging_add_status(self):
        recipe_status = TeamBoiling.Logging.Logging.add_recipe_status
        self.assertEquals(recipe_status, 'test')

    if __name__ == '__main__':
        unittest.main()
