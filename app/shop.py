from datetime import datetime
from typing import Dict, Any


class Shop:
    def __init__(
            self,
            info: Dict[str, Any],
            location: str
    ) -> None:
        self.location = location
        self.name = info.get["name", ""]
        self.products = info.get["product", []]

    def check_printing(
            self,
            customer: Any,
    ) -> None:
        current = datetime.datetime.now()
        timestamp = f"Date: {current.strftime('%d/%m/%Y %H:%M:%S')}"

        print(f"{timestamp.strip()}")
        customer.location = self.location
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        spent_money = 0
        for product, amount in customer.product_cart.items():
            if product in self.products:
                cost = self.products[product] * amount
                spent_money += cost
                if isinstance(cost, float):
                    cost = int(cost)
                print(f"{amount} {product}s for {cost} dollars")

        print(f"Total cost is {spent_money} dollars\nSee you again!")
