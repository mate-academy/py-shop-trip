import datetime
from typing import Dict, List


def format_price(price: float) -> str:
    price_float = float(price)  # upewniamy się, że to float
    if price_float.is_integer():
        return str(int(price_float))
    else:
        return str(price_float)


class Shop:
    def __init__(
            self, name: str, location: List[int], products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: Dict[str, int]) -> float:
        return sum(
            self.products[prod] * qty for prod, qty in product_cart.items()
        )

    def print_receipt(
            self, customer_name: str, product_cart: Dict[str, int]
    ) -> None:
        print(
            f'\nDate: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0.0
        for product, qty in product_cart.items():
            price = self.products[product]
            cost = float(price * qty)
            print(f"{qty} {product}s for {format_price(cost)} dollars")
            total += cost
        print(f"Total cost is {format_price(total)} dollars")
        print("See you again!")
