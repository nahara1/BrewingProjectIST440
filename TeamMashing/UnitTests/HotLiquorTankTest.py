# Project: Brewing Project
# Purpose Details: UnitTests for HotLiquorTank
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 4/10/2020
# Last Date Changed: 4/21/2020
# Rev: 2.0
import unittest

from TeamMashing.HotLiquorTank import HotLiquorTank
from TeamMashing.RecipeMashing import recipe_mashing

class HotLiquorTankTest(unittest.TestCase):
    def test_check_water_temp(self):
        hlt = HotLiquorTank()
        rm = recipe_mashing()
        self.assertEqual(hlt.water_temp, rm.water_temp)

    def test_check_water_volume(self):
        hlt = HotLiquorTank()
        rm = recipe_mashing()
        self.assertEqual(hlt.water_amount, rm.water_amount)