from utilities import get_median
from settings import ITEM, COUNT


class ShoppingCart(object):
    """
    Class to represent a shopping cart
    """
    def __init__(self):
        super(ShoppingCart, self).__init__()
        self._items = {}

    @property
    def total_cost(self):
        """total price of all items in the cart, returned to 2 decimal places as its a price"""
        return round(sum([val[ITEM].price * val[COUNT] for val in self._items.values()]), 2)

    @property
    def total_item_count(self):
        return sum([val[COUNT] for val in self._items.values()])

    def get_item(self, item_name):
        if self._items.get(item_name, None):
            return self._items[item_name][ITEM]

    def get_item_count(self, item_name):
        if self._items.get(item_name, None):
            return self._items[item_name][COUNT]
        else:
            return 0

    def insert_item(self, item):
        if not self._items.get(item.name, None):
            self._items[item.name] = {ITEM: item, COUNT: 1}
        else:
            self._items[item.name][COUNT] += 1

    def delete_item(self, item_name):
        if self._items.get(item_name, None):
            self._items[item_name][COUNT] -= 1
            if self._items[item_name][COUNT] <= 0:
                del self._items[item_name]

    def delete_item_all(self, item_name):
        """removes all items from the cart of specified type"""
        if self._items.get(item_name, None):
            del self._items[item_name]

    def get_median_price(self, round_price=True):
        """
        :arg round_price: bool to determine if median price should be rounded
                to 2 decimal places or not
         """
        prices = []
        for val in self._items.values():
            prices.extend([val[ITEM].price for i in range(val[COUNT])])
        median = get_median(prices)
        if round_price and median:
            median = round(median, 2)
        return median

    def clear_cart(self):
        self._items = {}
