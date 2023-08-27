from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @staticmethod
    def calculate_distance(
            start_point: list[int],
            end_point: list[int]
    ) -> float:
        x1, y1 = start_point
        x2, y2 = end_point

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def calculate_trip_cost(
            self,
            departure_location: list[int],
            arrival_location: list[int],
            fuel_price: float
    ) -> float:
        distance = self.calculate_distance(
            departure_location,
            arrival_location
        )
        return distance * self.fuel_consumption / 100 * fuel_price
