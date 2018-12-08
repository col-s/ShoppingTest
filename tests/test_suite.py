import unittest
from test_shopping_cart import ShoppingCartTest
from test_utilities import UtilitiesTest


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ShoppingCartTest))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UtilitiesTest))
    return test_suite


def run():
    unittest.TextTestRunner().run(suite())


if __name__ == '__main__':
    run()
