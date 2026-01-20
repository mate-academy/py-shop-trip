from __future__ import annotations


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def from_dict(cls, car: dict) -> Car:
        return cls(
            car.get("brand"),
            car.get("fuel_consumption")
        )

    def __repr__(self) -> str:
        return f"{self.brand}"
