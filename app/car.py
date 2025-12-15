from __future__ import annotations


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self._brand = brand
        self._fuel_consumption = fuel_consumption

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    @staticmethod
    def from_dict(car_dict: dict) -> Car:
        return Car(
            brand=car_dict.get("brand"),
            fuel_consumption=car_dict.get("fuel_consumption")
        )

    def __repr__(self) -> str:
        return (f"Car(brand='{self._brand}', "
                f"fuel_consumption={self._fuel_consumption})")
