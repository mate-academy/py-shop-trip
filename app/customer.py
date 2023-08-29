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


def create_customer(customer_data: Dict) -> Customer:
    return Customer(**customer_data)
