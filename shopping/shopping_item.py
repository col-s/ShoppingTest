class ShoppingItem(object):
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
        return '{0}: {1}'.format(self._name, self._price)
