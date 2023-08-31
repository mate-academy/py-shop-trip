from __future__ import annotations
from dataclasses import dataclass
from typing import Union
import math


@dataclass
class Car:
    brand: str
    fuel_consumption: Union[int, float]

    @classmethod
    def create_car_object(cls, dict_of_car: dict) -> Car:
        return cls(
            dict_of_car.get("brand"), dict_of_car.get("fuel_consumption")
        )

    @staticmethod
    def calculate_distance(
        location1: list[int], location2: list[int]
    ) -> float:
        return math.sqrt(
            (location2[0] - location1[0]) ** 2
            + (location2[1] - location1[1]) ** 2
        )

    def make_fuel_calculation(
        self, customer_coords: list[int], shop_coords: list[int]
    ) -> float:
        distance_to_shop = self.calculate_distance(
            customer_coords, shop_coords
        )

        fuel_used_round_trip = (self.fuel_consumption / 100) * (
            distance_to_shop * 2
        )

        return round(fuel_used_round_trip * Car.fuel_price, 2)


# test = Car("BMW", 9.9)
# Car.fuel_price = 2.4
# print(test.make_fuel_calculation([12, -2], [10, -5]))
