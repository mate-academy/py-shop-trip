from typing import Union, List

from app.Car import Car


class Customer:
    customers = {}

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[int],
            money: Union[int, float],
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        Customer.customers[self.name] = self
