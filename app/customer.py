from __future__ import annotations
from dataclasses import dataclass
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float | int

    def buy_in_shop(self, min_cost: int | float, data_shop: Shop) -> None:
        print()
        # print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for key, value in self.product_cart.items():
            cost_result = data_shop.cost_products[key] * value
            if (cost_result - int(cost_result)) == 0:
                cost_result = int(cost_result)
            print(f"{value} {key}s for {cost_result} dollars")
            total_cost += cost_result
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - min_cost} dollars")
        print()
