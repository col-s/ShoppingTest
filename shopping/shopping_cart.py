import logging
from utilities import get_median
from settings import ITEM, COUNT, PRICE, NAME


class ShoppingCart(object):
    """
    Class to represent a shopping cart
    """
    def __init__(self):
        super(ShoppingCart, self).__init__()
        self._items = {}

    @property
    def total_cost(self):
        """total price of all items in the cart, rounded to 2 decimal places"""
        return round(sum([val[ITEM].price * val[COUNT] for val in self._items.values()]), 2)

    @property
    def total_item_count(self):
        return sum([val[COUNT] for val in self._items.values()])

    def get_item(self, item_name):
        if self._items.get(item_name, None):
            print(self._items[item_name][ITEM])
            return self._items[item_name][ITEM]

    def get_item_count(self, item_name):
        if self._items.get(item_name, None):
            return self._items[item_name][COUNT]
        else:
            return 0

    def get_item_price(self, item_name):
        if self._items.get(item_name, None):
            return round(self._items[item_name][ITEM].price, 2)
        else:
            return 0.0

    def get_item_total_cost(self, item_name):
        if self._items.get(item_name, None):
            return round(self._items[item_name][ITEM].price * self._items[item_name][COUNT], 2)
        else:
            return 0.0

    def insert_item(self, item):
        """
        :arg item: ShoppingItem object
        """
        if not self.validate_item(item):
            return
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
            prices.extend([val[ITEM].price for _ in range(val[COUNT])])
        median = get_median(prices)
        if round_price and median:
            median = round(median, 2)
        return median

    def clear_cart(self):
        self._items = {}

    @staticmethod
    def validate_item(item):
        if not hasattr(item, NAME):
            logging.error('Missing shopping item attribute {0}.'.format(NAME))
            return False
        if not hasattr(item, PRICE):
            logging.error('Shopping item {0} has no price.'.format(item.name))
            return False
        if not isinstance(item.price, int) and not isinstance(item.price, float):
            logging.error('Invalid item price for {0}.'.format(item.name))
            return False
        return True

    def __str__(self):
        prefix = 'ShoppingCart:'
        if self._items:
            items = ['{} x{}'.format(self._items[key][ITEM].name,
                                     self._items[key][COUNT]) for key in self._items.keys()]
            items.sort()
            return '{} {}'.format(prefix, ', '.join(items))
        else:
            return '{} empty'.format(prefix)
