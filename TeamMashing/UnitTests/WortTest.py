# Project: Brewing Project
# Purpose Details: UnitTests for HotLiquorTank
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 4/10/2020
# Last Date Changed: 4/21/2020
# Rev: 2.0

import datetime
import time
import unittest

from TeamMashing.Wort import Wort
from TeamMashing.RecipeMashing import recipe_mashing

class WortTest(unittest.TestCase):
    def test_check_hot_water(self):
        w = Wort()
        rm = recipe_mashing()
        self.assertEqual(w.hot_water_temp, rm.water_temp)

    def test_check_water_volume(self):
        w = Wort()
        rm = recipe_mashing()
        self.assertEqual(w.water_volume, rm.water_amount)

    def test_check_wort_volume(self):
        w = Wort()
        rm = recipe_mashing()
        self.assertEqual(w.wort_volume, rm.wort_volume)

    def test_separate_wort(self):
        w = Wort()
        rm = recipe_mashing()
        self.assertEqual(w.separation_time, rm.separation_time)