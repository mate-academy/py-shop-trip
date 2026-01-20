from __future__ import annotations
from dataclasses import dataclass
from typing import List

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_card: dict
    location: list
    money: float | int
    car: Car

    def buy(self, shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        cheapest_shop = None
        cheapest_cost = 1000000
        for shop in shops:
            road_cost = (self.car.trip_distance(self.location, shop.location)
                         * self.car.fuel_consumption / 100
                         * self.car.fuel_price)
            total_cost = round(
                road_cost * 2 + shop.get_price(self.product_card), 2
            )
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
            if total_cost < cheapest_cost:
                cheapest_shop = shop
                cheapest_cost = total_cost
        if cheapest_cost > self.money:
            print(f"{self.name} doesn't have enough money to "
                  f"make a purchase in any shop")
            return
        print(f"{self.name} rides to {cheapest_shop.name}")
        print("")
        cheapest_shop.give_receipt(self.name, self.product_card)
        print("")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - cheapest_cost} dollars")
        print("")
