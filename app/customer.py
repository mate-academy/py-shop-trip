from math import sqrt
from typing import Any

from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def count_check(
            self,
            shop: Any,
    ) -> float:
        milk = self.product_cart["milk"] * shop.products["milk"]
        bread = self.product_cart["bread"] * shop.products["bread"]
        butter = self.product_cart["butter"] * shop.products["butter"]
        result = milk + bread + butter
        return result

    def trip(self, shop: Any, fuel_price: float) -> float:
        return round(
            sqrt(
                pow(self.location[0] - shop.location[0], 2)
                + pow(self.location[1] - shop.location[1], 2)
            ) * self.car.fuel_consumption / 100 * 2 * fuel_price
            + self.count_check(shop),
            2
        )

    def acting(self, shops: list, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        ct_ = []
        for shop in shops:
            ct_.append(self.trip(shop, fuel_price))
            print(f"{self.name}'s trip to the {shop.name} costs {ct_[-1]:.2f}")

        min_value = min(ct_)
        shop_min_cost = shops[ct_.index(min(ct_))]
        if min_value < self.money:
            print(f"{self.name} rides to {shop_min_cost.name}", end="\n\n")
            shop_min_cost.print_check(self)
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money - min_value} dollars")
            print()
        else:
            print(f"{self.name} doesn't have enough", end=" ")
            print("money to make a purchase in any shop")
