from math import dist


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_required_fuel(self, location_a: list,
                                location_b: list) -> float:
        return 2 * dist(location_a, location_b) * self.fuel_consumption / 100
