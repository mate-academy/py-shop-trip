from __future__ import annotations


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def from_dict(cls, car_dict: dict) -> Car:
        return cls(
            car_dict.get("brand"),
            car_dict.get("fuel_consumption")
        )
