from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    @staticmethod
    def from_dict(car_dict: dict) -> Car:
        return Car(
            car_dict["brand"],
            car_dict["fuel_consumption"]
        )
