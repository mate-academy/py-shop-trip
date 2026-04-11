from app.car import Car
from app.location import Location
from app.product import Product


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
        self.product_cart = Product(**product_cart)
        self.location = Location(*location)
        self.money = money
        self.car = Car(**car)
        self.shop_lowest_price = None
