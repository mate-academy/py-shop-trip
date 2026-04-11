from __future__ import annotations
from dataclasses import dataclass
from typing import Union


@dataclass
class Product:
    milk: float
    bread: float
    butter: float

    def price_for_milks(self, milk_price: Product) -> Union[float, int]:
        price = self.milk * milk_price.milk
        if price == int(price):
            return int(price)
        return price

    def price_for_breads(self, bread_price: Product) -> Union[float, int]:
        price = self.bread * bread_price.bread
        if price == int(price):
            return int(price)
        return price

    def price_for_butters(self, butter_price: Product) -> Union[float, int]:
        price = self.butter * butter_price.butter
        if price == int(price):
            return int(price)
        return price

    def price_for_all(self, price: Product) -> float | int:
        return (self.price_for_milks(price)
                + self.price_for_breads(price)
                + self.price_for_butters(price))
