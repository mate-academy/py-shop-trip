from dataclasses import dataclass
import datetime
from typing import Any


@dataclass
class Shop:

    name: str
    location: list
    products: dict

    @classmethod
    def config_from_dict(cls, config: dict) -> "Shop":
        return cls(
            config["name"],
            config["location"],
            config["products"],
        )

    def shopping_cost(self, product_cart: dict) -> float:
        cost = 0
        for product in product_cart:
            cost += self.products[product] * product_cart[product]

        return cost

    def take_client(
            self,
            customer: Any
    ) -> None:
        print("Date: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, amount in customer.product_cart.items():
            product_cost = self.products[product] * amount
            if product_cost == int(product_cost):
                product_cost = int(product_cost)
            print(f"{amount} {product}s for "
                  f"{product_cost} dollars")
        total_cost = self.shopping_cost(customer.product_cart)
        customer.money -= total_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
