from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_price: float
    fuel_consumption: float

    @property
    def full_price(self) -> float:
        return self.fuel_price * (self.fuel_consumption / 100)
