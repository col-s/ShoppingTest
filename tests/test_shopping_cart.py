import unittest
from shopping.shopping_cart import ShoppingCart


class ShoppingCartTest(unittest.TestCase):
    """Unit tests for Shopping cat"""

    def setUp(self):
        self.shopping_cart = ShoppingCart()

    def tearDown(self):
        pass

    def test_get_item(self):
        pass

    def test_get_item_count(self):
        pass

    def test_insert_item(self):
        pass

    def test_delete_item(self):
        pass

    def test_get_median_price(self):
        pass


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ShoppingCartTest))
    return test_suite


def run():
    unittest.TextTestRunner().run(suite())


if __name__ == '__main__':
    run()
