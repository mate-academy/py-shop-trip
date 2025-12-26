# shop.py
from dataclasses import dataclass
import datetime
from typing import List, Dict

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, int]

    def calculate_product_cost(self, product_cart: dict[str, int]) -> float:
        total_cost = sum(
            self.products[product] * quantity
            for product, quantity in product_cart.items()
            if product in self.products
        )
        return total_cost

    def give_check(self, customer: Customer) -> str:
        product_cart = customer.product_cart
        total_cost = self.calculate_product_cost(product_cart)
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        check = (f"Date: {current_date}\n"
                 f"Thanks, {customer.name}, for your purchase!\n"
                 f"You have bought:\n")
        for product, quantity in product_cart.items():
            if product in self.products:
                price = self.products[product] * quantity
                price_str = int(price) if price == int(price) else price
                check += f"{quantity} {product}s for {price_str} dollars\n"
        check += (f"Total cost is {total_cost} dollars\n"
                  f"See you again!\n")
        return check
