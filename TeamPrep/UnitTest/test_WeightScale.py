# Project: Brewing Automation System - Capstone Project
# Purpose Details: Temperature Unit Test
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 4/22
# Last Date Changed:4/22
# Rev

import unittest
from TeamPrep import WeightScale

w = WeightScale


class TestWeightScale(unittest.TestCase):
    def test_read_weight_grains(self):
        self.assertTrue(w)

    def test_read_weight_hops(self):
        self.assertTrue(w)


if __name__ == '__main__':
    unittest.main()
