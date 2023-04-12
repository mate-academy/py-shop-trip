from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int, int],
            money: float,
            car: Car,
    ) -> None:
        self._name = name
        self.product_cart = product_cart
        self.location = location
        self._money = money
        self.car = car

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_money(self) -> float:
        return self._money
