from __future__ import annotations

from math import dist


class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def from_dict(cls, car: dict) -> Car:
        return cls(brand=car["brand"],
                   fuel_consumption=car["fuel_consumption"])

    def fuel_cost(self,
                  first_point: list[int],
                  last_point: list[int],
                  one_liter_price: float) -> int | float:
        return round(dist(first_point, last_point)
                     * self.fuel_consumption
                     * one_liter_price
                     * 2
                     / 100,
                     2)
