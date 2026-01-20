from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def is_money_enough(self, shop: Shop) -> True:
        if self.money >= shop.total_price(
                self.product_cart
        ) and shop.is_all_product_in_shop(self.product_cart):
            return True
        return False

    def customer_to_shop(self, shop: Shop) -> None:
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def customer_to_home(self, money_spent: float) -> None:
        print(f"{self.name} rides home")
        self.money -= money_spent
        print(f"{self.name} now has {self.money} dollars\n")
