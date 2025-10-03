import datetime

from dataclasses import dataclass
from typing import List, Dict

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, float]

    def calculate_cart_price(self, cart: Dict[str, int]) -> float:
        total = 0.0
        for product, quantity in cart.items():
            price = self.products.get(product)
            if price is None:
                raise KeyError(f"There isn't any {product}s in {self.name}.")
            total += quantity * price
        return int(total) if total == int(total) else total

    def print_receipt(self, customer: Customer) -> float:
        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total = 0.0
        for product in customer.product_cart:
            price_for_one_product = self.products[product]
            quantity = customer.product_cart[product]
            cost = quantity * price_for_one_product
            if cost == int(cost):
                cost = int(cost)
            print(f"{quantity} {product}s for {cost} dollars")
            total += cost
        total = round(total, 2)
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
        return total
