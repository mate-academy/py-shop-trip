from __future__ import annotations


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def from_dict(cls, dictionary: dict) -> Car:
        return cls(dictionary["brand"], dictionary["fuel_consumption"])
