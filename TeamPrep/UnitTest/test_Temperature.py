# Project: Brewing Automation System - Capstone Project
# Purpose Details: Temperature Unit Test
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/7
# Rev

import unittest
from TeamPrep import Temperature

t = Temperature


class TestTemperature(unittest.TestCase):
    def test_read_temp(self):
        self.assertTrue(t)


if __name__ == '__main__':
    unittest.main()
