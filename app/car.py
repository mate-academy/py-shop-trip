import math


class Car:

    def __init__(self, brand: str, fuel_consumption: float,
                 location: list[int]) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.location = [location[0], location[1]]
        self.current_trip = 0

    @staticmethod
    def get_distance(start: list, destination: list) -> float:
        return math.dist(start, destination)

    def get_consumption_for_the_trip(self, distance: float) -> float:
        return self.fuel_consumption * distance / 100

    def move_to_destination(self, destination: list[int]) -> None:
        distance = self.get_distance(self.location, destination)
        self.location[0] = destination[0]
        self.location[1] = destination[1]
        self.current_trip += distance

    def finish_trip(self) -> float:
        fuel_spent = self.get_consumption_for_the_trip(self.current_trip)
        self.current_trip = 0

        return fuel_spent
