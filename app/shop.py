import datetime
from typing import List
from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: List[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def sale_of_goods(self, customer: Customer) -> None:
        customer.location = self.location

        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought: ")

        total_cost = 0
        for product, amount in customer.product_cart.items():
            total_cost += (amount * self.products[product])
            print(f"{amount} {product}s for "
                  f"{amount * self.products[product]} dollars")

        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!\n")

    def __repr__(self) -> str:
        return self.name
