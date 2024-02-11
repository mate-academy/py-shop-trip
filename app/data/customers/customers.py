from app.data.customers.cars.car import Car
from app.data.location import Location
from app.data.product_cart import ProductCart


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = ProductCart(**product_cart)
        self.location = Location(*location)
        self.money = money
        self.car = Car(**car)
