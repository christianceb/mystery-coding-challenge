from unittest import TestCase
from solution import search

class Test_TestSearch(TestCase):
    def test_search(self):
        list = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]

        for i in list:
            self.assertTrue(self.csr(i, list))

        self.assertFalse(self.csr(69, list))
        self.assertFalse(self.csr(-100, list))
        self.assertFalse(self.csr(100, list))

    def csr(self, value, list):
        """ C(oalesce) S(earch) R(esult)

        Executes solution.search() and coalesces search result from positive integers (including zero)
        to return true, false if received None

        :param value: value to search
        :param list: list to search the value from
        :return: True if a result was found, False if received none.
        """
        return True if not search(value, list) is None else False