import unittest
from shopping.utilities import sort_numbers, get_median


class UtilitiesTest(unittest.TestCase):
    """Unit tests for Utilities"""

    def setUp(self):
        self.number_list = [5, 7, 9, 5, 3, 2, 4, 5]

    def test_sort_numbers(self):
        sort_numbers(self.number_list)
        self.assertEqual([2, 3, 4, 5, 5, 5, 7, 9], self.number_list)

    def test_get_median(self):
        self.assertEqual(5, get_median(self.number_list))
        self.assertEqual(5, get_median(self.number_list))
