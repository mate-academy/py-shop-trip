import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def count_trip(self,
                   fuel_price: float,
                   from_location: list[int],
                   to_location: list[int]) -> float:
        distance = math.dist((from_location[0], from_location[1]),
                             (to_location[0], to_location[1]))
        fuel = distance * (self.fuel_consumption / 100)
        return fuel * fuel_price
