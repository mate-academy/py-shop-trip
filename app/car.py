from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def km_price(self) -> float:
        return self.fuel_consumption / 100
