import math

from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def distance(self, shop: Shop) -> int | float:
        return math.dist(self.location, shop.location) * 2

    def cost_distance(self, car: Car, shop: Shop, fuel_price: float) -> float:
        car_km_cost = car.km_cost()
        return (
            self.distance(shop)
            * car_km_cost
            * fuel_price
        )

    def calculate_product_cost(
            self,
            shop: Shop,
            product: str,
            quantity: int
    ) -> float:
        return quantity * self.product_cart[product]

    def cost_products(self, shop: Shop) -> float:
        total_cost = 0
        for product, quantity in shop.products.items():
            total_cost += self.calculate_product_cost(shop, product, quantity)
        return total_cost

    def total_costs(self, car: Car, shop: Shop, fuel_price: float) -> float:
        return round(
            self.cost_products(shop)
            + self.cost_distance(car, shop, fuel_price), 2
        )
