from typing import Dict, Any
import datetime


class Shop:
    def __init__(
            self,
            info: Dict[str, Any],
    ) -> None:
        self.name = info["name"]
        self.location = info["location"]
        self.products = info["products"]

    def check_printing(
            self,
            customer: Any,
    ) -> str:
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
                if cost % 1 == 0:
                    cost = int(cost)
                print(f"{amount} {product}s for {cost} dollars")
        print(f"Total cost is {spent_money} dollars\nSee you again!\n")
