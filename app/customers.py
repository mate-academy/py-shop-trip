from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: tuple[int, int],
            money: float,
            car: Car
    ) -> None:
        self._name = name
        self._product_cart = product_cart
        self._location = location
        self._money = money
        self._car = car

    @property
    def name(self) -> str:
        return self._name

    @property
    def product_cart(self) -> dict[str, int]:
        return self._product_cart

    @property
    def location(self) -> tuple[int, int]:
        return self._location

    @location.setter
    def location(self, new_location: tuple[int, int]) -> None:
        if (
                len(new_location) == 2
                and all(isinstance(x, int) for x in new_location)
        ):
            self._location = new_location

    @property
    def money(self) -> int | float:
        return round(self._money, 2)

    @property
    def car(self) -> Car:
        return self._car

    def spend(self, amount: float) -> None:
        if amount > self._money:
            raise ValueError("Not enough money")
        self._money -= amount
