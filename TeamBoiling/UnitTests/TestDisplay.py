# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Erik Ellis (eae5206@psu.edu)
# Date Developed: 4/11/2020
# Last Date Changed: 4/11/2020
# Rev 1

import unittest
from TeamBoiling import DisplayHelper

class TestDisplay(unittest.TestCase):

    def test_print_start_info(self):
        DisplayHelper.print_start_info('01:01:01', 10, 105, True)

    def test_print_end_info(self):
        DisplayHelper.print_end_info('02:02:02', 10)


if __name__ == '__main__':
    unittest.main()