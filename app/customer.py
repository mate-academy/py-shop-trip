from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            products_want_buy: dict,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products_want_buy = products_want_buy
        self.money = money
        self.car = car