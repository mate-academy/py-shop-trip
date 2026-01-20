from __future__ import annotations


class Car:
    def __init__(self, *args, **kwargs) -> None:
        car = None
        if args and isinstance(args[0], dict):
            car = args[0]
        elif isinstance(kwargs, dict):
            car = kwargs

        if car is not None:
            self.brand = car["brand"]
            self.fuel_consumption = car["fuel_consumption"]
        else:
            raise TypeError

    def calculate_fuel(self, distance: float) -> float:
        return self.fuel_consumption * distance / 100
