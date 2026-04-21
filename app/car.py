from __future__ import annotations


class Car:
    def __init__(self, brand: str, fuel: float) -> None:
        self.brand = brand
        self.fuel = fuel

    def __str__(self) -> str:
        return f"Car(brand={self.brand}, fuel={self.fuel})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, item: dict) -> Car:
        return cls(brand=item["brand"], fuel=item["fuel_consumption"])
