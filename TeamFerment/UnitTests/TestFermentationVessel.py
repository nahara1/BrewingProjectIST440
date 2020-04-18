# Project: IST 440 Barlog Brewery
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/16/20
# Last Date Changed: 4/16/20
# Rev: 1

import unittest
from TeamFerment.FermentationVessel import FermentationVessel

ferment_vessel = FermentationVessel()


class FermentationVesselTest(unittest.TestCase):

    def test_original_gravity(self):
        orig_gravity = ferment_vessel.get_original_gravity()
        self.assertTrue(1.000 <= orig_gravity <= 1.06)

    def test_final_gravity(self):
        final_gravity = ferment_vessel.get_final_gravity()
        self.assertTrue(1.01 <= final_gravity <= 1.02)


if __name__ == '__main__':
    unittest.main()
