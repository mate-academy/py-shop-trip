from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def fuel_cost(self, distance: float, fuel_price: float) -> float:
        liters = (distance / 100) * self.fuel_consumption
        cost = liters * fuel_price
        return cost
