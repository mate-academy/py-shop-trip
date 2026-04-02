from typing import Dict, Any
from decimal import Decimal, ROUND_HALF_UP


class Car:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.brand: str = data["brand"]
        self.fuel_consumption: Decimal = Decimal(str(data["fuel_consumption"]))

    def fuel_cost(self, distance: float, fuel_price: float) -> Decimal:
        distance_dec: Decimal = Decimal(str(distance))
        fuel_price_dec: Decimal = Decimal(str(fuel_price))
        cost: Decimal = (
            self.fuel_consumption / Decimal("100")
            * distance_dec
            * fuel_price_dec
        )
        return cost.quantize(Decimal("0.01"), ROUND_HALF_UP)
