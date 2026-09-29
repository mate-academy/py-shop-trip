from dataclasses import dataclass
import math

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: Car

    def distance(self, shop: Shop) -> float:
        customer_x, customer_y = self.location
        shop_x, shop_y = shop.location

        return math.sqrt(
            (customer_x - shop_x) ** 2
            + (customer_y - shop_y) ** 2
        )

    def cost_of_the_trip(
        self,
        shop: Shop,
        fuel_price: float,
    ) -> float:
        distance = self.distance(shop)
        fuel_cost = self.car.fuel_cost(
            distance * 2,
            fuel_price,
        )
        product_cost = shop.total_price_of_products(
            self.product_cart,
        )

        return fuel_cost + product_cost

    def can_buy_from(self, shop: Shop) -> bool:
        return all(
            product in shop.products
            for product in self.product_cart
        )
