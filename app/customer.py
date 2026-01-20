from app.car import Car


class Customer:

    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    def __str__(self) -> str:
        return (f"{self.name} has {self.car} and has to buy "
                f"{', '.join([product for product in self.products])}")
