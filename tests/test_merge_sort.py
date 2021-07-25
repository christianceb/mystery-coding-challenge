from unittest import TestCase
from solution import merge_sort

class Test_TestMergeSort(TestCase):
    def test_merge_sort_1(self):
        unsorted = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        answer_key = sorted(unsorted)

        self.assertEqual(answer_key, merge_sort(unsorted))

    def test_merge_sort_pt1_a1(self):
        unsorted = [13, 5, 6, 2, 5]
        answer_key = [2, 5, 6, 13]

        self.assertEqual(answer_key, merge_sort(unsorted))

    def test_merge_sort_pt1_a2(self):
        unsorted = [5, 2, 5, 13]
        answer_key = [2, 5, 13]

        self.assertEqual(answer_key, merge_sort(unsorted))

    def test_merge_sort_pt2_a1(self):
        unsorted = [14, 27, 1, 4, 2, 50, 3, 1]
        answer_key = [1, 2, 3, 4, 14, 27, 50]

        self.assertEqual(answer_key, merge_sort(unsorted))

    def test_merge_sort_pt2_a2(self):
        unsorted = [2, 4, -4, 3, 1, 1, 14, 27, 50]
        answer_key = [-4, 1, 2, 3, 4, 14, 27, 50]

        self.assertEqual(answer_key, merge_sort(unsorted))

    def test_merge_sort_deduplication(self):
        unsorted = [13, 13, 5, 6, 2, 5]
        answer_key = [2, 5, 6, 13]

        self.assertEqual(answer_key, merge_sort(unsorted))