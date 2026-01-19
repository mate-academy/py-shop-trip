from __future__ import annotations
from math import sqrt


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def create_car(cls, car_info: dict) -> Car:
        try:
            return cls(car_info["brand"], car_info["fuel_consumption"])
        except KeyError as e:
            print(e, "not exist")

    def calculate_cost_one_way(
        self, fuel_price: float, home_location: list, shop_location: list
    ) -> float:
        distance = sqrt(
            (shop_location[0] - home_location[0]) ** 2
            + (shop_location[1] - home_location[1]) ** 2
        )
        return ((self.fuel_consumption * distance) / 100) * fuel_price
