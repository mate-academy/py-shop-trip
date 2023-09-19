from typing import Dict, Any


class Car:
    def __init__(self, info: Dict[str, Any], fuel_price: float) -> None:
        self.brand = info["brand"]
        self.fuel_consumption = float(info["fuel_consumption"])
        self.fuel_price = float(fuel_price)

    def calculate_fuel_cost(self, distance: float) -> float:
        fuel_amount = 2 * (self.fuel_consumption / 100) * distance
        return round(fuel_amount * self.fuel_price, 2)
