import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def serve(self, customer: "Customer") -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product in customer.product_cart:
            price = customer.product_cart[product] * self.products[product]
            print(
                f"{customer.product_cart[product]} "
                f"{product}s for {price:g} dollars"
            )
            total_cost += price
        customer.money -= total_cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
