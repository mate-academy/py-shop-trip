from __future__ import annotations


class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.consumption = fuel_consumption

    @classmethod
    def from_dict(cls, car_info: dict) -> Car:
        return cls(car_info["brand"], car_info["fuel_consumption"])
