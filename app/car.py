from __future__ import annotations


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_trip_cost(self, distance: float, fuel_price: float) -> float:
        return distance / 100 * self.fuel_consumption * fuel_price

    @classmethod
    def from_dict(cls, car: dict) -> Car:
        return cls(
            brand=car.get("brand"),
            fuel_consumption=car.get("fuel_consumption")
        )
