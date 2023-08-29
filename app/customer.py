from __future__ import annotations
from typing import Dict, List


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict,
            location: List[int],
            money: float,
            car: Dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.fuel_consumption = car["fuel_consumption"]

    @classmethod
    def create_customer(cls, customer_data: Dict) -> Customer:
        return Customer(**customer_data)
