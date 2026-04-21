from app.car import Car


class Customer:
    def __init__(
            self, name: str, location: list,
            money: float, car: Car, products: dict) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.car = car
        self.products = products
