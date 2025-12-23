from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_cost(
            self,
            distance: int | float, fuel_price: int | float
    ) -> float:

        fuel_consumed = distance / 100 * self.fuel_consumption
        return fuel_consumed * fuel_price
