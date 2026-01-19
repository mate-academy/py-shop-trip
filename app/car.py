from __future__ import annotations


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def create_car(cls, car_info: dict[str, str | float | int]) -> Car:
        return cls(
            brand=car_info["brand"],
            fuel_consumption=car_info["fuel_consumption"]
        )

    def calculate_fuel_consumption(self, distance: float) -> float:
        return (self.fuel_consumption / 100) * distance
