from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self._name = name
        self._products = products
        self._location = location
        self.money = money
        self._car = car

    @property
    def name(self) -> str:
        return self._name

    @property
    def products(self) -> dict:
        return self._products

    @property
    def location(self) -> list[int]:
        return self._location

    @property
    def money(self) -> int:
        return self._money

    @money.setter
    def money(self, money: int) -> None:
        self._money = money

    @property
    def car(self) -> Car:
        return self._car
