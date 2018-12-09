import unittest
from shopping.shopping_cart import ShoppingCart
from shopping.shopping_item import ShoppingItem


class ShoppingCartTest(unittest.TestCase):
    """Unit tests for Shopping Cart"""

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        self.apple = ShoppingItem('apple', 0.15)
        self.banana = ShoppingItem('banana', 0.50)
        self.orange = ShoppingItem('orange', 0.25)
        self.shopping_cart.insert_item(self.apple)
        self.shopping_cart.insert_item(self.banana)

    def tearDown(self):
        self.shopping_cart.clear_cart()

    def test_total_price(self):
        self.assertEqual(0.65, self.shopping_cart.total_cost)
        self._add_oranges()
        self.assertEqual(1.90, self.shopping_cart.total_cost)
        self.shopping_cart.clear_cart()
        self.assertEqual(0.00, self.shopping_cart.total_cost)

    def test_total_item_count(self):
        self.assertEqual(2, self.shopping_cart.total_item_count)
        self._add_oranges()
        self.assertEqual(7, self.shopping_cart.total_item_count)
        self.shopping_cart.clear_cart()
        self.assertEqual(0, self.shopping_cart.total_item_count)

    def test_get_item(self):
        self.assertEqual(self.apple, self.shopping_cart.get_item('apple'))

    def test_get_item_count(self):
        self.assertEqual(1, self.shopping_cart.get_item_count('apple'))
        self._add_oranges()
        self.assertEqual(5, self.shopping_cart.get_item_count('orange'))
        self.assertEqual(0, self.shopping_cart.get_item_count('foo'))

    def test_insert_item(self):
        self.shopping_cart.insert_item(self.orange)
        self.assertEqual(self.orange, self.shopping_cart.get_item('orange'))

    def test_delete_item(self):
        self.shopping_cart.delete_item('banana')
        self.assertEqual(None, self.shopping_cart.get_item('banana'))
        self.assertEqual(0, self.shopping_cart.get_item_count('banana'))
        self._add_oranges()
        self.assertEqual(5, self.shopping_cart.get_item_count('orange'))
        self.shopping_cart.delete_item('orange')
        self.assertEqual(4, self.shopping_cart.get_item_count('orange'))

    def test_delete_item_all(self):
        self._add_oranges()
        self.assertEqual(5, self.shopping_cart.get_item_count('orange'))
        self.shopping_cart.delete_item_all('orange')
        self.assertEqual(0, self.shopping_cart.get_item_count('orange'))

    def test_get_median_price(self):
        self.assertEqual(0.33, self.shopping_cart.get_median_price())
        self.assertEqual(0.325, self.shopping_cart.get_median_price(round_price=False))
        self.shopping_cart.insert_item(self.orange)
        self.assertEqual(0.25, self.shopping_cart.get_median_price())
        self.shopping_cart.delete_item('orange')
        self.shopping_cart.delete_item('banana')
        self.assertEqual(0.15, self.shopping_cart.get_median_price())
        self.shopping_cart.delete_item('apple')
        self.assertEqual(None, self.shopping_cart.get_median_price())

    def test_clear_cart(self):
        self.shopping_cart.clear_cart()
        self.assertEqual({}, self.shopping_cart._items)
        self.assertEqual(0, self.shopping_cart.total_item_count)

    def _add_oranges(self):
        for i in range(5):
            self.shopping_cart.insert_item(self.orange)
