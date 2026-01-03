from __future__ import annotations


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
            fuel_price: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
