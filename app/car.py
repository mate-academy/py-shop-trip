from dataclasses import dataclass


@dataclass
class Car:
    name: str
    fuel_consumption: float | int

    def total_cost_of_fuel(self, distance: float | int, fuel_price: float | int) -> float:
        return (self.fuel_consumption * distance / 100) * fuel_price
