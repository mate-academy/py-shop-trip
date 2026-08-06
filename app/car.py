from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Car:
    FUEL_PRICE: ClassVar[float] = field()
    brand: str
    fuel_consumption: float

    def fuel_cost(self, distance: float) -> float:
        return self.FUEL_PRICE * self.fuel_consumption * distance / 100

    @classmethod
    def set_fuel_price(cls, price: float) -> None:
        cls.FUEL_PRICE = price
