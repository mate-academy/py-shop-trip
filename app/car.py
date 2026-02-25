from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def fuel_cost(self, distances: float, fuel_price: float) -> float:
        consumption_per_1_km = self.fuel_consumption / 100
        litres = distances * consumption_per_1_km
        cost = litres * fuel_price
        return cost
