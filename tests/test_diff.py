from unittest import TestCase
from solution import diff

class Test_TestDiff(TestCase):
    def test_diff(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 4, 5, 6]

        answer_key = [1, 6]

        self.assertEqual(diff(x, y), answer_key)