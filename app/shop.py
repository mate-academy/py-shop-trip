from typing import TYPE_CHECKING
from math import fsum

if TYPE_CHECKING:
    from customer import Customer


class Shop:

    def __init__(
        self,
        name: str,
        location: list[int],
        products: dict[str, int]
    ) -> None:
        self.name = name
        self.location = location.copy()
        self.products = products.copy()

    def print_purchase_info(
        self,
        customer: "Customer",
        total_cost: float
    ) -> None:
        print(
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer.name}, for your purchase!"
        )

        print("You have bought:")

        for name, count in customer.product_cart.items():
            cost = self.products[name] * count
            if cost == int(cost):
                cost = int(cost)
            print(f"{count} {name}s for {cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    def get_purchase_cost(self, customer: "Customer") -> float:
        return fsum(
            customer.product_cart[name] * self.products[name]
            for name in customer.product_cart
        )
