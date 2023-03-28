import datetime
from typing import List

from app.customer import Customer


class Shop:
    def __init__(self, shop_dict: dict) -> None:
        self.name: str = shop_dict["name"]
        self.location: List[int] = shop_dict["location"]
        self.products: dict = shop_dict["products"]

    def bill(self, customer: Customer) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"Date: {date}\n"
            f"Thanks, {customer.name}, for your purchase!"
        )
        print("You have bought:")
        total_costs = 0
        for product, number in customer.product_cart.items():
            price = self.products[product] * number
            print(f"{number} {product}s for {price} dollars")
            total_costs += price
        print(
            f"Total cost is {total_costs} dollars\n"
            f"See you again!\n"
        )

    def products_sum(self, customer: Customer) -> int:
        return sum(
            product * price
            for product, price
            in zip(customer.product_cart.values(), self.products.values())
        )
