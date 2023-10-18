from typing import Dict, Any


class Car:
    def __init__(
            self,
            info: Dict[str, Any],
            fuel_price: float,
    ) -> None:
        self.brand = info["brand"]
        self.fuel_consumption = info["fuel_consumption"]
        self.fuel_price = float(fuel_price)
