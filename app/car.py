from typing import Dict, Any


class Car:
    def __init__(self, info: Dict[str, Any], fuel_price: float) -> None:
        self.brand = info["brand"]
        self.fuel_consumption = info["fuel_consumption"]
        self.fuel_price = float(fuel_price)

    def calculate_fuel_cost(self, distance: float) -> float:
        fuel_amount = (distance / 100) * self.fuel_consumption \
            * self.fuel_price * 2
        return round(fuel_amount, 2)
