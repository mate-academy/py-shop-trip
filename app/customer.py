import datetime


from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_card: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_card = product_card
        self.location = location
        self.money = money
        self.car = car


    def shop_tier(self, shops: list[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")

