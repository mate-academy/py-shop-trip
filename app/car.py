from math import sqrt


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_trip_price(
        self,
        fuel_price: float,
        current_location: list[float],
        target_location: list[float],
    ) -> float:
        distance: float = sqrt(
            (target_location[0] - current_location[0]) ** 2
            + (target_location[1] - current_location[1]) ** 2
        )
        fuel_used: float = distance * (self.fuel_consumption / 100)
        return fuel_used * fuel_price
