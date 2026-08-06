from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Car:
    FUEL_PRICE: ClassVar[float] = 0.0
    brand: str
    fuel_consumption: float

    def fuel_cost(self, distance: float) -> float:
        return self.FUEL_PRICE * self.fuel_consumption * distance / 100
