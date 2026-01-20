class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
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
    def product_cart(self) -> dict:
        return self._product_cart

    @property
    def location(self) -> list:
        return self._location

    @property
    def money(self) -> int:
        return self._money

    @property
    def car(self) -> dict:
        return self._car

    def money_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def less_money_info(self) -> None:
        print(f"{self.name} doesn't have enough money"
              f" to make purchase in any shop")
