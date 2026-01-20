from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            products_to_buy: dict,
            location: list[int],
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])
