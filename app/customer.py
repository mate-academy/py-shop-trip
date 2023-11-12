from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from app.shop import Shop
from app.user_data import get_data


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
        user_x, user_y = self.location
        shop_x, shop_y = other.location
        return round(
            (sqrt((shop_x - user_x) ** 2
                  + (shop_y - user_y) ** 2)) * 2, 2
        )

    def fuel(self) -> float:
        fuel_price = float(get_data()["FUEL_PRICE"])
        return (self.car["fuel_consumption"] / 100) * fuel_price

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
