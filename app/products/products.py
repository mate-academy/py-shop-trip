from typing import Union


class Products:
    def __init__(self, name: str, price: Union[int, float]):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: Union[int, float]):
        self._price = price
