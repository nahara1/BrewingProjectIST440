# Project: Brewing Project
# Purpose Details: UnitTests for MillingMachine
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 4/10/2020
# Last Date Changed: 4/21/2020
# Rev: 2.0

import unittest
import datetime
import time

from TeamMashing.MillingMachine import MillingMachine
from TeamMashing.RecipeMashing import recipe_mashing

class MillingMachineTest(unittest.TestCase):
    def test_check_grains_weight(self):
        m = MillingMachine()
        rm = recipe_mashing()
        self.assertEqual(m.grains_weight, rm.grains_weight)

    def test_mill_grains(self):
        m = MillingMachine()
        rm = recipe_mashing()
        self.assertEqual(m.mill_time, rm.mill_time)
