from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_cost_way(self, way: float, fuel_price: float) -> float | int:
        return (way / 100) * self.fuel_consumption * fuel_price
