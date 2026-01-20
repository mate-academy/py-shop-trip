from typing import Dict, Any


class Car:
    FUEL_PRICE = 2.4

    def __init__(self, data: Dict[str, Any]) -> None:
        self.brand = data["brand"]
        self.fuel_consumption = data["fuel_consumption"]
