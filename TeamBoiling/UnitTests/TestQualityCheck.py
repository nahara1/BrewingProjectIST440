# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/16/2020
# Last Date Changed: 4/22/20
# Rev 2

import unittest
from TeamBoiling import QualityCheck


class TestQualityCheck(unittest.TestCase):

    def test_get_qa_check_pass(self):
        quality_checked = input("Test QA Check: ")
        self.assertEqual(quality_checked, 'Yes')
        QualityCheck.QualityCheck.get_QA_Check(quality_checked)

    def test_get_qa_check_fail(self):
        quality_checked = input("Test QA Check: ")
        self.assertEqual(quality_checked, 'No')
        QualityCheck.QualityCheck.get_QA_Check(quality_checked)

