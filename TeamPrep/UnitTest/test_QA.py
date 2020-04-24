import unittest
from TeamPrep import QualityCheck_Prep

q = QualityCheck_Prep


class TestSanitization(unittest.TestCase):

    def test_QA(self):
        self.assertTrue(q)


if __name__ == '__main__':
    unittest.main()
