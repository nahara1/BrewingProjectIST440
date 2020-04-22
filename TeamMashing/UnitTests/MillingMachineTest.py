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
