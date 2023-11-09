import math


class Car:
    fuel_price = 0

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_ride_cost_to(
            self,
            location: list,
            destination: list
    ) -> float:
        distance = math.sqrt(math.pow(destination[0] - location[0], 2)
                             + math.pow(destination[1] - location[1], 2))
        return distance * (self.fuel_consumption / 100) * Car.fuel_price
