import numpy as np
from typing import List




class Car:
    def __init__(self, name: str, fuel_consumption: float) -> None:
        self.name = name
        self.fuel_consumption = fuel_consumption

    def ride_cost(self, start_location: List[int], end_location: List[int], fuel_price: float) -> float:
        start_point = np.array(start_location)
        end_point = np.array(end_location)
        fuel_per_km = self.fuel_consumption / 100
        distance = np.linalg.norm(end_point - start_point)
        fuel_per_ride = distance * fuel_per_km
        price = fuel_per_ride * fuel_price
        return price
