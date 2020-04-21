# Project: Brewing Project
# Purpose Details: Kegging Tasks Class Test
# Course: IST 440W
# Author: Team Kegging - Aaleem Siddiqui
# Date Developed: 4/18/2020
# Last Date Changed: 4/18/2020
# Rev: 1.0

import unittest
from TeamKegging.KeggingTasks import KeggingTasks


class TestKeggingTasks(unittest.TestCase):
    def test_batch_ID(self):
        kt1 = KeggingTasks(1234, "Default", "CELLARMAN_READY")
        self.assertEqual(kt1.batch_id, 1234)


if __name__ == '__main__':
    unittest.main()
