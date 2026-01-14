import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_distance(
            self,
            own_location: list,
            destination: list
    ) -> float:
        distance = math.sqrt(
            (own_location[0] - destination[0]) ** 2
            + (own_location[1] - destination[1]) ** 2
        )
        return distance

    def calculate_fuel_cost(
            self,
            distance: float,
            fuel_consumption_per_100km: float,
            fuel_price: float
    ) -> float:
        fuel_needed = (distance / 100) * fuel_consumption_per_100km
        return fuel_needed * fuel_price
