from math import dist


class Car:
    def __init__(
        self,
        brand: str,
        fuel_consumption: float,
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __str__(self) -> str:
        return (
            f"Car ({self.brand}, {self.fuel_consumption})"
        )

    def trip_cost(
        self,
        start: int,
        end: int,
        fuel_price: int | float,
    ) -> int | float:
        distance = dist(start, end)
        fuel_needed = (distance / 100) * self.fuel_consumption
        return fuel_needed * fuel_price
