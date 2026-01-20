from app.car import Car
from decimal import Decimal
import math


class Customer():
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: Decimal,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance(self, shop_location: list) -> float:
        return math.sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2)

    def ride_home(self, spend_money: float) -> None:
        print(f"{self.name} rides home")
        money_after_shop = self.money - spend_money
        self.money = money_after_shop
        print(f"{self.name} now has {money_after_shop} dollars\n")
