from datetime import datetime
from decimal import Decimal
from typing import Any

# from app.car import Car
from app.shop import Shop


class Customer:

    list_customer = []

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: Decimal,
            car: Any
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def will_cost(self, one_shop: Shop) -> list[float]:
        total_cost = []
        for product, count in self.product_cart.items():
            price_per_unit = one_shop.products.get(product)
            total_cost.append(count * price_per_unit)
        return total_cost

    def create_check(self, one_shop: Shop) -> None:
        total_cost = self.will_cost(one_shop)

        current_datatime = datetime(2021, 1, 4, 12, 33, 41)
        current_datatime = current_datatime.strftime("%d/%m/%Y %H:%M:%S")
        milk = self.product_cart.get("milk")
        bread = self.product_cart.get("bread")
        butter = self.product_cart.get("butter")
        print(f"Date: {current_datatime}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        print(f"{milk} milks for {total_cost[0]} dollars")
        if total_cost[1] == int(total_cost[1]):
            total_cost[1] = int(total_cost[1])
        print(
            f"{bread} "
            f"breads for {total_cost[1]} dollars"
        )
        print(
            f"{butter} "
            f"butters for {total_cost[2]} dollars"
        )
        print(f"Total cost is {sum(total_cost)} dollars")
        print("See you again!\n")

    def custom_at_home(self, money_spent: float) -> None:
        cost_now = round(Decimal(self.money) - Decimal(money_spent), 2)

        print(f"{self.name} rides home")
        print(f"{self.name} now has {cost_now} dollars\n")
