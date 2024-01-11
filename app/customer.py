from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def primary_amount_of_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def print_rides_home(self) -> None:
        print(f"{self.name} rides home")

    def final_amount_of_money(self) -> None:
        print(f"{self.name} now has {self.money} dollars\n")
