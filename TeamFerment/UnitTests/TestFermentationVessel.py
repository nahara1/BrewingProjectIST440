import unittest
from TeamFerment.FermentationVessel import FermentationVessel

ferment_vess = FermentationVessel()

class FermentationVesselTest(unittest.TestCase):

    def test_original_gravity(self):
        orig_gravity = ferment_vess.get_original_gravity()
        self.assertTrue(1.000 <= orig_gravity <= 1.06)


    def test_final_gravity(self):
        final_gravity = ferment_vess.get_final_gravity()
        self.assertTrue(1.01 <= final_gravity <= 1.02)


if __name__ == '__main__':
    unittest.main()
