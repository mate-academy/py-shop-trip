from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    def print_money(self) -> None:
        return print(f"{self.name} has {self.money} dollars")

    def go_home(self) -> None:
        print(f"{self.name} rides home")
