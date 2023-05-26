from dataclasses import dataclass
from app.car import Car
from app.shop import Shop
from math import sqrt


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: dict | Car

    def __post_init__(self) -> None:
        if isinstance(self.car, dict):
            self.car = Car(**self.car)

    def cost_to_shop(self, shop: Shop, fuel_price: float) -> float:
        leg_along_x = (self.location[0] - shop.location[0])
        leg_along_y = (self.location[1] - shop.location[1])
        diagonal = sqrt(leg_along_x ** 2 + leg_along_y ** 2)
        return diagonal / 100 * fuel_price * self.car.fuel_consumption * 2

    def cost_of_products(self, shop: Shop) -> float:
        return sum(product_amount * shop.products[product_name]
                   for product_name, product_amount
                   in self.product_cart.items())

    def shopping(self, shop: Shop) -> dict:
        products_data = {}
        total = 0
        for name, amount in self.product_cart.items():
            cost = amount * shop.products[name]
            products_data[name] = (amount, cost)
            total += cost
        products_data["total_cost"] = total
        return products_data
