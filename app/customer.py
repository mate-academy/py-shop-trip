from math import sqrt


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float,
        car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(
        self,
        dest: list
    ) -> float:
        return sqrt(
            (self.location[0] - dest[0]) ** 2
            + (self.location[1] - dest[1]) ** 2
        )
