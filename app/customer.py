from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            products_to_buy: dict[str, int],
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = car
