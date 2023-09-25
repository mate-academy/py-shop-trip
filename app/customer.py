from __future__ import annotations

from typing import Dict, List


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: List[int],
            money: int,
            car: Dict[str, str | float]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
