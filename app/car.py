from dataclasses import dataclass
import math

from app.convert import FUEL_PRICE


@dataclass
class Car:
    brand: str
    fuel_consumption: float
    fuel_price = FUEL_PRICE

    def fuel_outgo(self, shop_loc: list, customer_loc: list) -> int | float:
        return round((
                    (self.fuel_consumption / 100
                     * math.dist(customer_loc, shop_loc))
            * self.fuel_price) * 2, 2
        )
