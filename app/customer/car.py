from dataclasses import dataclass
from typing import Self


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @classmethod
    def from_dict(cls, car: dict) -> Self:
        return cls(
            brand=car["brand"], fuel_consumption=car["fuel_consumption"]
        )
