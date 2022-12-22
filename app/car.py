from __future__ import annotations


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def count_trip_cost(
            customer_location: list,
            shop_location: list,
            fuel_consumption: float,
            fuel_price: float
    ) -> float:
        x1, y1 = customer_location
        x2, y2 = shop_location
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        trip_cost = distance * (fuel_consumption / 100) * fuel_price * 2
        return trip_cost
