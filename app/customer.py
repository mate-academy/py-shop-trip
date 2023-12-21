from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict = None,
                 location: list = None,
                 money: int | float = None) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self._car = None

    @property
    def car(self) -> Car | None:
        return self._car

    @car.setter
    def car(self, car: Car) -> None:
        self._car = car

    def spend_money(self, money: int | float) -> None:
        self.money -= money
