# Project: Brewing Project
# Purpose Details: Brite Tank Test
# Course: IST 440W
# Author: Team Kegging - Ronald Salguero
# Date Developed: 4/14/2020
# Last Date Changed: 4/14/2020
# Rev: 1.0

import unittest
from TeamKegging.KeggingBriteTank import KeggingBriteTank

test_keg = KeggingBriteTank(1, 33, 5, 5, 12, "START")


class TestBriteTank(unittest.TestCase):
    def test_temperature(self):
        test_temp = test_keg.auto_temp(35, 1)

        self.assertEqual(test_temp, 35)

    def test_pressure(self):
        test_psi = test_keg.auto_psi(12, 1)

        self.assertEqual(test_psi, 12)

    def test_carbonation(self):
        test_keg.auto_carb(2.8, 1)
        test_carb = test_keg.get_carbonation()
        self.assertEqual(test_carb, 2.84)


if __name__ == '__main__':
    unittest.main()
