from typing import Dict, Any
from decimal import Decimal


class Car:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.brand: str = data["brand"]
        self.fuel_consumption = Decimal(str(data["fuel_consumption"]))

    def fuel_cost(self, distance: float, fuel_price: float) -> Decimal:
        distance = Decimal(str(distance))
        fuel_price = Decimal(str(fuel_price))

        cost = (self.fuel_consumption / Decimal("100")) * distance * fuel_price
        return cost
