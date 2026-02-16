from typing import List
import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(
            self,
            loc1: List[float],
            loc2: List[float],
            fuel_value: float
    ) -> float:
        distance_km = (
            math.sqrt((loc2[0] - loc1[0])**2 + ((loc2[1] - loc1[1])**2))
        )
        liters_spent = ((self.fuel_consumption / 100) * distance_km)
        return liters_spent * fuel_value
