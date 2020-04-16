import datetime
import unittest
import time

from TeamMashing.SpargingTank import SpargingTank
from Brewing.MongoLog import Log
from TeamMashing.Wort import Wort
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


