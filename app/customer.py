import dataclasses
import math
from typing import Any


FUEL_PRICE = 2.4


@dataclasses.dataclass
class Customer:
    name: str
    products: dict
    location: tuple
    money: int
    car: dict

    @staticmethod
    def fuel_shop(fuel_cons: float, distance_to_shop: float) -> float:
        return ((fuel_cons * distance_to_shop) / 100 * FUEL_PRICE) * 2

    def dist_shop(self, shop_location: tuple) -> float:
        return (
            math.sqrt((shop_location[0] - self.location[0]) ** 2
                      + (shop_location[1] - self.location[1]) ** 2)
        )

    def prod_count(self) -> Any:
        return self.products.values()

    def prod_choice(self, product_price: callable) -> None:
        for product, value in self.products.items():
            for price in product_price:
                prod_sum = value * price
                print(f"{value} {product} for {prod_sum} dollars")
