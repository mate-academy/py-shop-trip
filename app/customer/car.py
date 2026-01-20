import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_ride_cost_to(
            self,
            location: list[int],
            destination: list[int],
            fuel_price: float
    ) -> float:
        distance = math.sqrt(math.pow(destination[0] - location[0], 2)
                             + math.pow(destination[1] - location[1], 2))
        return distance * (self.fuel_consumption / 100) * fuel_price
