from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str: int],
            location: list,
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)  # Create an instance of the Car class
