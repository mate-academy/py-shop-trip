import math


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: int
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def calculate_distance(
            location_start: list[int],
            location_end: list[int]
    ) -> float:
        return math.sqrt((location_end[0] - location_start[0]) ** 2
                         + (location_end[1] - location_start[1]) ** 2)

    def calculate_trip_cost(self, distance: float, fuel_price: float) -> float:
        return distance / 100 * self.fuel_consumption * fuel_price
