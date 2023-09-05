from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @classmethod
    def from_dict(cls, car: dict) -> Car:
        return Car(
            brand=car["brand"], fuel_consumption=car["fuel_consumption"]
        )
