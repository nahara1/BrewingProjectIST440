# Project: Brewing Automation System - Capstone Project
# Purpose Details: Sanitization Unit Test
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/7
# Rev


import unittest
from  TeamPrep import Sanitization
s = Sanitization
class TestSanitization(unittest.TestCase):

    def test_sanitization(self):
        self.assertTrue(s)

if __name__ == '__main__':
    unittest.main()


