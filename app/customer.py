import json

import math

from dataclasses import dataclass

import app.shop as mall
from app.cart import Cart
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: list[Cart]
    location: list[int]
    money: float
    car: Car

    def calculate_trip_to_shop(self, shop: mall) -> float:
        fuel_consumption = self.car.fuel_consumption
        distance = self._count_distance(shop.location)
        trip_cost = round(fuel_consumption * distance * 2
                          / 100 * self._get_fuel_price(), 2)

        return trip_cost

    def print_report(self, shops: list[mall]) -> str:
        shop_dict = {}
        result = f"{self.name} has {self.money} dollars\n"

        for shop in shops:
            trip_sum = (self.calculate_trip_to_shop(shop)
                        + shop.print_receipt(self)[1])
            shop_dict[shop.name] = trip_sum

            result += (
                f"{self.name}'s trip to the {shop.name} costs {trip_sum}\n")

        min_sum_trip = min(shop_dict.values())

        if self.money >= min_sum_trip:

            self.money -= min_sum_trip

            prefer_shop = min(shop_dict, key=shop_dict.get)
            result += f"{self.name} rides to {prefer_shop}\n\n"

            for shop in shops:
                if shop.name == prefer_shop:
                    result += shop.print_receipt(self)[0] + "\n"

            result += (f"\n{self.name} rides home\n"
                       f"{self.name} now has {self.money} dollars\n\n")

        else:
            result += (f"{self.name} doesn't have enough money "
                       f"to make purchase in any shop\n\n")

        return result

    def _count_distance(self, shop_coords: list) -> float:
        x1, y1 = self.location
        x2, y2 = shop_coords
        return math.hypot(x2 - x1, y2 - y1)

    @staticmethod
    def _get_fuel_price() -> float:
        with open("config.json", "r") as data_file:
            data_from_file = json.loads(data_file.read())
        return data_from_file.get("FUEL_PRICE")
