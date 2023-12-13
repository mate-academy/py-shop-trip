import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def print_check(self, customer_name: str, customer_products: dict) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")

        cost_total = 0
        for product, count in customer_products.items():
            cost = count * self.products[product]
            cost_total += cost
            print(f"{count} {product}s for {cost} dollars")
        print(f"Total cost is {cost_total} dollars")
        print("See you again!\n")
