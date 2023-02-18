from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: int | float

    @classmethod
    def get_car_info(cls, car: dict) -> Car:
        return cls(
            brand=car["brand"],
            fuel_consumption=car["fuel_consumption"]
        )
