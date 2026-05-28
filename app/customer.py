from dataclasses import dataclass

from app.location import Location
from app.car import Car


class NotEnoughMoneyError(Exception):
    pass


@dataclass
class Customer:
    _name: str
    _product_cart: dict
    _location: Location
    _money: float | int
    _car: Car

    @property
    def name(self) -> str:
        return self._name

    @property
    def balance(self) -> float | int:
        return self._money

    @property
    def location(self) -> Location:
        return self._location

    @property
    def product_cart(self) -> dict:
        return self._product_cart

    @property
    def car(self) -> Car:
        return self._car

    def pay(self, amount: float | int) -> None:
        if amount > self._money:
            raise NotEnoughMoneyError(
                f"Cannot pay {amount} $. {self.name} has only {self.balance}"
            )
        self._money -= amount

    def drive_to(self, destination: Location) -> None:
        self._location = destination

    def refuel(self, destination: Location, fuel_price: float | int) -> None:
        amount = self.car.get_fuel_cost(self.location, destination, fuel_price)
        self.pay(amount)
