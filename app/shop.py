import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def _fmt(value: float) -> str:
        return str(int(value)) if value % 1 == 0 else str(value)

    def calculate_cart_cost(self, product_cart: dict) -> float:
        total_price = 0
        for product, quantity in product_cart.items():
            total_price += quantity * self.products[product]
        return total_price

    def print_receipt(self, customer: "Customer", cart_item: dict) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, quantity in cart_item.items():
            price = self.products[product]
            cost = price * quantity
            print(f"{quantity} {product}s for {self._fmt(cost)} dollars")

        total = self.calculate_cart_cost(cart_item)
        print(f"Total cost is {self._fmt(total)} dollars")
        print("See you again!")
        print()
