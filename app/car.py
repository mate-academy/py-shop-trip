import math


class Car:

    def __init__(self, brand: str, fuel_consumption_100_km: float) -> None:
        self.brand = brand
        self.fuel_consumption_100_km = fuel_consumption_100_km

    def fuel_price_per_trip(self, distance: float, fuel_price: float) -> float:
        return (distance * self.fuel_consumption_100_km / 100) * fuel_price

    @staticmethod
    def calculate_distance(initial_position: list[float],
                           destination_position: list[float]) -> float:
        return math.dist(initial_position, destination_position)
