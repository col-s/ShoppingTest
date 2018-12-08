import unittest
from shopping.shopping_cart import ShoppingCart
from shopping.shopping_item import ShoppingItem


class ShoppingCartTest(unittest.TestCase):
    """Unit tests for Shopping cart"""

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        self.apple = ShoppingItem('apple', 0.15)
        self.banana = ShoppingItem('banana', 0.50)
        self.orange = ShoppingItem('orange', 0.25)
        self.shopping_cart.insert_item(self.apple)
        self.shopping_cart.insert_item(self.banana)

    def tearDown(self):
        self.shopping_cart = ShoppingCart()

    def test_get_item(self):
        self.assertEqual(self.apple, self.shopping_cart.get_item('apple'))

    def test_get_item_count(self):
        self.assertEqual(1, self.shopping_cart.get_item_count('apple'))
        for i in range(5):
            self.shopping_cart.insert_item(self.orange)
        self.assertEqual(5, self.shopping_cart.get_item_count('orange'))
        self.assertEqual(0, self.shopping_cart.get_item_count('foo'))

    def test_insert_item(self):
        self.shopping_cart.insert_item(self.orange)
        self.assertEqual(self.orange, self.shopping_cart.get_item('orange'))

    def test_delete_item(self):
        self.shopping_cart.delete_item('banana')
        self.assertEqual(None, self.shopping_cart.get_item('banana'))
        self.assertEqual(0, self.shopping_cart.get_item_count('banana'))

    def test_get_median_price(self):
        self.assertEqual(0.325, self.shopping_cart.get_median_price())
        self.shopping_cart.insert_item(self.orange)
        self.assertEqual(0.25, self.shopping_cart.get_median_price())
        self.shopping_cart.delete_item('orange')
        self.shopping_cart.delete_item('banana')
        self.assertEqual(0.15, self.shopping_cart.get_median_price())
        self.shopping_cart.delete_item('apple')
        self.assertEqual(None, self.shopping_cart.get_median_price())
