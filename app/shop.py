from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list[float]
    products: dict[str, float]

    def can_fulfill(self, cart: dict[str, int]) -> bool:
        return all(product in self.products for product in cart)

    def cart_cost(self, cart: dict[str, int]) -> float:
        total = 0.0
        for product, qty in cart.items():
            total += qty * self.products[product]
        return total

    def print_receipt(self, customer_name: str, cart: dict[str, int]) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, qty in cart.items():
            line = qty * self.products[product]
            print(f"{qty} {product}s for {line:g} dollars")

        total = self.cart_cost(cart)
        print(f"Total cost is {total:g} dollars")
        print("See you again!")
        print()
