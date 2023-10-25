import json


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand,
        self.fuel_consumption = fuel_consumption

    def calculate_trip_coast(self, distance: float, data: json) -> float:
        fuel_cost = data.get("FUEL_PRICE")
        return distance / 100 * self.fuel_consumption * fuel_cost
