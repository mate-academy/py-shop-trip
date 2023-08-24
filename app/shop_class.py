import datetime
from typing import List, Dict


class Shop:
    def __init__(self,
                 name: str,
                 location: List[int],
                 products: Dict[str, int]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: str) -> None:
        date_now = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
        print(
            f"Date: {date_now}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: "
        )
        total_cost = 0
        for product in customer.products_cart:
            quantity = customer.products_cart[product]
            cost = quantity * self.products[product]
            total_cost += cost
            product_name = product
            currency = "dollar"
            if quantity > 1:
                product_name = f"{product_name}s"
            if cost > 1:
                currency = f"{currency}s"
            print(f"{quantity} {product_name} for {cost} {currency}")
        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )
