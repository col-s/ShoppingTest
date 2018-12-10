class ShoppingItem(object):
    """
    Class to be a generic representation of items of shopping
    Specific items would be sub-classed based on this
    NOTE: Class created to use solely in testing of ShoppingCart
    :arg name: string of the item name, used to identify the item
    :arg price: int or float of the price of the item,
                currency is not specified
    """
    def __init__(self, name, price):
        super(ShoppingItem, self).__init__()
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def __str__(self):
        return '{}, price={:.2f}'.format(self._name, self._price)

    def __repr__(self):
        return 'ShoppingItem({}, {})'.format(self._name, self._price)
