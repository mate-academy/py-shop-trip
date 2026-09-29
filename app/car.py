from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def fuel_cost(
        self,
        distance: float,
        fuel_price: float,
    ) -> float:
        fuel_needed = distance * self.fuel_consumption / 100

        return fuel_needed * fuel_price
