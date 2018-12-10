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
        self.shopping_cart.insert_item(ShoppingItem('bar', 0))
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

    def test_get_item_price(self):
        self.assertEqual(0.15, self.shopping_cart.get_item_price('apple'))
        self.assertEqual(0.0, self.shopping_cart.get_item_price('foo'))
        int_price = ShoppingItem('bar', 1)
        self.shopping_cart.insert_item(int_price)
        self.assertEqual(1.0, self.shopping_cart.get_item_price('bar'))
        self.assertTrue(isinstance(self.shopping_cart.get_item_price('bar'), float))

    def test_get_item_total_cost(self):
        self.assertEqual(0.15, self.shopping_cart.get_item_total_cost('apple'))
        self._add_oranges()
        self.assertEqual(1.25, self.shopping_cart.get_item_total_cost('orange'))
        self.assertEqual(0.0, self.shopping_cart.get_item_total_cost('foo'))

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

    def test_validate_item(self):
        self.assertTrue(ShoppingCart.validate_item(self.orange))
        invalid_price = ShoppingItem('foo', None)
        self.assertFalse(ShoppingCart.validate_item(invalid_price))
        self.assertFalse(ShoppingCart.validate_item(str))
        self.shopping_cart.insert_item(invalid_price)
        self.assertEqual(0, self.shopping_cart.get_item_count('foo'))

    def test__str__(self):
        self.assertEqual('ShoppingCart: apple x1, banana x1', str(self.shopping_cart))
        self._add_oranges()
        self.assertEqual('ShoppingCart: apple x1, banana x1, orange x5', str(self.shopping_cart))
        self.shopping_cart.clear_cart()
        self.assertEqual('ShoppingCart: empty', str(self.shopping_cart))

    def _add_oranges(self):
        for i in range(5):
            self.shopping_cart.insert_item(self.orange)
