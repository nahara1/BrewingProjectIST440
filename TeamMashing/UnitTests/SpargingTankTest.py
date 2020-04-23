# Project: Brewing Project
# Purpose Details: UnitTests for SpargingTank
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 4/10/2020
# Last Date Changed: 4/21/2020
# Rev: 2.0

import datetime
import unittest
import time

from TeamMashing.SpargingTank import SpargingTank
from TeamMashing.RecipeMashing import recipe_mashing

class SpargingTankTest(unittest.TestCase):
    def test_add_water(self):
        st = SpargingTank()
        rm = recipe_mashing()
        self.assertEqual(st.water_temp, rm.water_temp)

    def test_stir_mash(self):
        st = SpargingTank()
        rm = recipe_mashing()
        self.assertEqual(st.stir_time, rm.stir_time)


