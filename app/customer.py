from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from app.shop import Shop
from app.user_data import FUEL_PRICE


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: dict

    def get_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def get_distance(self, other: Shop) -> float:
        return round((sqrt(
            (other.location[0] - self.location[0]) ** 2
            + (other.location[1] - self.location[1]) ** 2)
                     ) * 2, 2)

    def fuel(self) -> float:
        return (self.car["fuel_consumption"] / 100) * FUEL_PRICE

    def product_cost(self, shops: list[Shop]) -> tuple:
        all_shops = {}

        for shop in shops:
            temp_dict = {
                key: self.product_cart[key]
                * shop.products[key]
                for key in self.product_cart
            }

            total_coast = sum(temp_dict.values())
            cost_trip = round(
                total_coast + (
                        self.fuel()
                        * self.get_distance(shop)
                ), 2
            )

            all_shops[(cost_trip, shop.name, total_coast)] = temp_dict.values()
            print(f"{self.name}'s trip to the {shop.name} costs {cost_trip}")
        best_shop = min(all_shops)
        return list(all_shops[best_shop]), best_shop
