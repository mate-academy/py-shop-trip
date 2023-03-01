import math
import json

import app.shop as shopi
from app.car import Car


class Customer:
    def __init__(self, name: str,
                 product_cart: list,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip(self, shop: shopi) -> float:
        fuel_consumption = self.car.fuel_consumption
        distance = self.count_distance(shop.location)
        trip_cost = round(fuel_consumption * distance * 2
                          / 100 * self.get_fuel_price(), 2)
        return trip_cost

    def print_message(self, shops: list) -> str:
        shop_dict = {}
        result = f"{self.name} has {self.money} dollars\n"

        for shop in shops:
            trip_sum = (self.calculate_trip(shop)
                        + shop.print_list(self)[1])
            shop_dict[shop.name] = trip_sum

            result += (f"{self.name}'s trip"
                       f" to the {shop.name}"
                       f" costs {trip_sum}\n")

        min_sum_trip = min(shop_dict.values())

        if self.money >= min_sum_trip:

            self.money -= min_sum_trip

            shop_to_choose = min(shop_dict, key=shop_dict.get)

            result += f"{self.name} rides to {shop_to_choose}\n\n"

            for shop in shops:
                if shop.name == shop_to_choose:
                    result += shop.print_list(self)[0] + "\n"

            result += (f"\n{self.name} rides home\n"
                       f"{self.name} now has {self.money} dollars\n\n")
        else:
            result += (f"{self.name} doesn't have enough money "
                       f"to make purchase in any shop\n\n")

        return result

    def count_distance(self, shop_coords: list) -> float:
        x1, y1 = self.location
        x2, y2 = shop_coords
        return math.hypot(x2 - x1, y2 - y1)

    @staticmethod
    def get_fuel_price() -> float:
        with open("app/config.json", "r") as data_file:
            data_from_file = json.loads(data_file.read())
        return data_from_file.get("FUEL_PRICE")
