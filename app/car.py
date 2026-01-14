from __future__ import annotations
from dataclasses import dataclass
from math import sqrt


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @classmethod
    def create_car(cls, car: dict) -> Car:
        return Car(
            car["brand"],
            car["fuel_consumption"]
        )

    def calculate_drive_cost(
        self,
        origin: list,
        destination: list,
        fuel_price: float
    ) -> float:
        distance = self.calculate_distance(origin, destination)
        return round((fuel_price * self.fuel_consumption * distance / 100), 2)

    @staticmethod
    def calculate_distance(start: list, goal: list) -> float:
        distance = sqrt((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2)
        return round(distance, 2)
