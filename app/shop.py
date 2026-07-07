import datetime
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


def fmt(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return str(round(value, 2))


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(
        self,
        cart: Dict[str, int]
    ) -> float:
        total = 0.0

        for item, qty in cart.items():
            total += self.products[item] * qty

        return total

    def print_receipt(
        self,
        customer: "Customer"
    ) -> None:
        current_time = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        total_cost = self.calculate_products_cost(
            customer.product_cart
        )

        print(f"\nDate: {current_time}")
        print(
            f"Thanks, {customer.name}, for your purchase!"
        )
        print("You have bought:")

        for item, qty in customer.product_cart.items():
            item_cost = self.products[item] * qty

            print(
                f"{qty} {item}s for {fmt(item_cost)} dollars"
            )

        print(
            f"Total cost is {fmt(total_cost)} dollars"
        )
        print("See you again!")
