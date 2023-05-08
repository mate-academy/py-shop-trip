from dataclasses import dataclass
import math


@dataclass
class Trip:
    name: str
    shop_location: list
    products: dict
    fuel_price: float
    fuel_consumption: float
    customer_location: list

    def money_for_products(self, product_cart: dict) -> dict:
        result = {}
        for product, value in product_cart.items():
            result[product] = value * self.products[product]
        return result

    def money_for_trip(self) -> int | float:
        distance_to_the_shop = math.sqrt(
            (self.shop_location[0] - self.customer_location[0]) ** 2
            + (self.shop_location[1] - self.customer_location[1]) ** 2
        )
        fuel = (distance_to_the_shop * self.fuel_consumption) / 100
        return round((fuel * self.fuel_price) * 2, 2)
