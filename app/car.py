from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float
    fuel_price: float

    def distance_cost(self, distance: float) -> float:
        costs_per_km = self.fuel_consumption / 100 * self.fuel_price
        distance_cost = round(costs_per_km * distance * 2, 2)
        return distance_cost
