# from numpy import median
from utilities import get_median
from settings import ITEM, COUNT


class ShoppingCart(object):
    """
    Class to represent a shopping cart
    """
    def __init__(self):
        super(ShoppingCart, self).__init__()
        self._items = {}

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
                self._items.pop(item_name)

    def get_median_price(self):
        prices = []
        for val in self._items.values():
            prices.extend([val[ITEM].price for i in range(val[COUNT])])
        return get_median(prices)
        # if prices:
        #     return median(prices)
