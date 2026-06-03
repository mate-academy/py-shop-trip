from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location.copy()

    @classmethod
    def from_dict(cls, dictionary: dict) -> Customer:
        return cls(
            name=dictionary["name"],
            product_cart=dictionary["product_cart"],
            location=dictionary["location"],
            money=dictionary["money"],
            car=Car.from_dict(dictionary["car"])
        )

    def relocate(self, location: list[int]) -> None:
        self.location = location

    def return_home(self) -> None:
        self.location = self.home_location

    def spend_money(self, amount_of_money: float) -> None:
        self.money -= amount_of_money
