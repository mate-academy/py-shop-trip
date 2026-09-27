from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def cost_for_1_km(self, fuel_price: float) -> float | int:
        return fuel_price * self.fuel_consumption / 100
