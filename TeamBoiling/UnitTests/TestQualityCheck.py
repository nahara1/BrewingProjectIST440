# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/16/2020
# Last Date Changed: 4/16/20
# Rev 1

import unittest
from TeamBoiling import QualityCheck


class TestQualityCheck(unittest.TestCase):

    def test_get_qa_check(self):
        test = QualityCheck.QualityCheck.get_QA_Check
        self.assertEqual(test, 'Yes')
