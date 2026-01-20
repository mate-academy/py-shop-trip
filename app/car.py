from math import dist


class Car:
    fuel_price = 0

    def __init__(self, brand: str, consumption: float, location: list) -> None:
        self.brand = brand
        self.consumption = consumption / 100
        self.location = location

    def trip_cost(self, destination: list) -> float:
        return dist(self.location, destination
                    ) * self.consumption * self.fuel_price
