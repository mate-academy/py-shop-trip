from .car import Car


class Customer:
    def __init__(self, name: str, location: list[int],
                 money: float, car: Car, product_cart: dict) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.car = car
        self.product_cart = product_cart
