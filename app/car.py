import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def ride_cost(
        self, start_point: list[int], destination: list[int], fuel_price: float
    ) -> float:
        start_x, start_y = start_point
        destination_x, destination_y = destination
        distance = math.sqrt(
            (destination_x - start_x) ** 2 + (destination_y - start_y) ** 2
        )
        cost_per_km = (self.fuel_consumption / 100) * fuel_price
        return cost_per_km * distance
