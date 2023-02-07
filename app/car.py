from __future__ import annotations


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def make_instance(cls, car: dict) -> Car:
        return cls(car["brand"],
                   car["fuel_consumption"])
