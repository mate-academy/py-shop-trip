from app.car import Car


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.product_cart = None
        self.location = []
        self.money = None
        self._car = None

    @property
    def car(self) -> Car:
        return self._car

    @car.setter
    def car(self, car: Car) -> None:
        self._car = car

    def spend_money(self, money: int | float) -> None:
        self.money -= money
