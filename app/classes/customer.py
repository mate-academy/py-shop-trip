from app.classes.car import Car
from app.classes.product import Products


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Products,
            location: list,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
