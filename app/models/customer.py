from .car import Car


class Customer:
    def __init__(
        self,
        name: str,
        location: list[float],
        money: float,
        car: Car,
        product_cart: dict[str, int]
    ) -> None:
        self.name = name
        self.location = tuple(location)
        self.money = money
        self.car = car
        self.product_cart = product_cart
