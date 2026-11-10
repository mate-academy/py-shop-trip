from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_round_trip_fuel_cost(
            self,
            distance: int | float,
            fuel_price: float
    ) -> float:
        if distance == 0 or fuel_price == 0:
            return 0
        fuel_used = (distance * 2) * self.fuel_consumption / 100
        return fuel_used * fuel_price
