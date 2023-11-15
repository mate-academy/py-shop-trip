import math

from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def distance_to_shop(self, shop: Shop) -> float:
        _a = self.location[0] - shop.location[0]
        _b = self.location[1] - shop.location[1]
        return math.sqrt(_a ** 2 + _b ** 2)

    def cost_to_shop(self, shop: Shop) -> float:
        _d = self.distance_to_shop(shop)
        return (_d * self.car.fuel_consumption) / 100

    def product_cost(self, shop: Shop) -> float:
        return sum(
            shop.products[product] * quantity
            for product, quantity in self.product_cart.items()
        )

    def print_product_list(self, shop: Shop) -> None:
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.product_cart.items():
            price = quantity * shop.products[product]
            if price == int(price):
                price = int(price)
            print(f"{quantity} {product}s for {price} dollars")
