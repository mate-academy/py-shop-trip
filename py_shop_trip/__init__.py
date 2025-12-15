import datetime
from typing import Optional


class Shop:
    def __init__(
        self,
        name: str,
        location: list[float],
        products: dict[str, float],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def can_fulfill(self, product_cart: dict[str, int]) -> bool:
        return all(product in self.products for product in product_cart)

    def calculate_total_cost(self, product_cart: dict[str, int]) -> float:
        return sum(
            self.products[product] * quantity
            for product, quantity in product_cart.items()
        )

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int],
        timestamp: Optional[datetime.datetime] = None,
    ) -> float:
        if timestamp is None:
            timestamp = datetime.datetime.now()

        print(f"\nDate: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Thank you, {customer_name}, for your purchase!")
        print("Items purchased:")

        total = 0.0
        for product, quantity in product_cart.items():
            unit_price = self.products.get(product, 0.0)
            price = unit_price * quantity
            print(f"{quantity} x {product} @ ${unit_price:.2f} = ${price:.2f}")
            total += price

        print(f"Total: ${total:.2f}")
        print("We hope to see you again!")
        return total
