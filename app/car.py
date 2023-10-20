from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float
    fuel_price = 0

    def gas_price(self, distance: float) -> float:
        return distance * self.fuel_consumption / 100 * Car.fuel_price
