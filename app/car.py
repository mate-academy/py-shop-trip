from typing import Dict, Any


class Car:
    def __init__(self, info: Dict[str, Any], fuel_price: float) -> None:
        self.brand = info["brand"]
        self.fuel_consumption = info["fuel_consumption"]
        self.fuel_price = fuel_price

    def calculate_trip_cost(self, start: list, end: list) -> float:
        distance = ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5
        return distance / 100 * self.fuel_consumption * self.fuel_price
