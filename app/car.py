from __future__ import annotations
from dataclasses import dataclass


@dataclass()
class Car:
    brand: str
    fuel_consumption: float

    @classmethod
    def car_object(cls, car: dict) -> Car:
        return Car(
            brand=car.get("brand"),
            fuel_consumption=car.get("fuel_consumption")
        )
