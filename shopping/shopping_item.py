class ShoppingItem(object):
    """
    Class to be a generic representation of items of shopping
    Specific items could be sub-classed from this
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

    def __repr__(self):
        return 'Name: {0}, Price: {1}'.format(self._name, self._price)
