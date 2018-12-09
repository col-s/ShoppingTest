import unittest
import random
from shopping.utilities import sort_numbers, get_median


class UtilitiesTest(unittest.TestCase):
    """Unit tests for Utilities"""

    def setUp(self):
        self.number_list = [5, 7, 9, 5, 3, 2, 4, 5]

    def test_sort_numbers(self):
        # test copy option
        sorted_numbers = sort_numbers(self.number_list, copy=True)
        self.assertEqual([2, 3, 4, 5, 5, 5, 7, 9], sorted_numbers)
        self.assertEqual([5, 7, 9, 5, 3, 2, 4, 5], self.number_list)
        # test standard operation (copy mode off)
        sort_numbers(self.number_list)
        self.assertEqual([2, 3, 4, 5, 5, 5, 7, 9], self.number_list)
        # test an already sorted list
        test_list = [1, 2, 3]
        sort_numbers(test_list)
        self.assertEqual([1, 2, 3], test_list)
        # test an empty list
        test_list = []
        sort_numbers(test_list)
        self.assertEqual([], test_list)
        # test a larger list
        test_list_rand = [random.randint(-100, 100) for i in range(0, 100000)]
        test_list_rand_result = sorted(test_list_rand)
        sort_numbers(test_list_rand)
        self.assertEqual(test_list_rand_result, test_list_rand)

    def test_get_median(self):
        self.assertEqual(5, get_median(self.number_list))
        # test empty list
        self.assertEqual(None, get_median([]))
        # test ints
        self.assertEqual(3, get_median([2, 4]))
        # test ints returning float
        self.assertEqual(2.5, get_median([2, 3]))
        # test floats
        self.assertEqual(2.75, get_median([2.1, 3.4]))

