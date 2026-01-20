from dataclasses import dataclass


@dataclass()
class Car:
    brand: str
    fuel_consumption: float

    def trip_cost(self, distance: float, fuel_price: float) -> float:
        return round(distance * self.fuel_consumption * fuel_price / 100, 3)
