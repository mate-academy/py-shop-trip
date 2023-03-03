from app.car import Car
from app.location import Location


class Customer:
    def __init__(
        self,
        name: str,
        money: int,
        car: dict,
        location: list[int],
        product_cart: dict
    ) -> None:
        self._name = name
        self._money = money
        self._car = Car(**car)
        self._start_location = Location(*location)
        self._location = self._start_location
        self._products = product_cart

    @property
    def name(self) -> str:
        return self._name

    @property
    def money(self) -> float:
        return self._money

    @property
    def car(self) -> Car:
        return self._car

    @property
    def location(self) -> Location:
        return self._location

    @property
    def products(self) -> dict:
        return self._products

    def __repr__(self) -> str:
        return (
            f"{self.name} has {self.money} $$ and {self.car}\n"
            f"- currently on {self.location} and needs {self.products}"
        )

    def pay(self, amount: float) -> None:
        self._money -= amount

    def ride(self, new_location: Location | str) -> None:
        if isinstance(new_location, str) and new_location == "back":
            self._location = self._start_location
        elif isinstance(new_location, Location):
            self._location = new_location
