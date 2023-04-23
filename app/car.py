from typing import Union


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: Union[int, float]
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = 0

    def fuel_cost_calculation_per_distance(self, distance: float) -> float:
        costs_per_km = self.fuel_consumption / 100 * self.fuel_price
        distance_cost = costs_per_km * distance * 2
        return round(distance_cost, 2)
