from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def total_product_price(self, products_to_buy: dict) -> float:
        return sum([quantity * self.products[product]
                    for product, quantity in products_to_buy.items()])

    def sell(self, cart: dict, customer_name: str) -> float:
        date = datetime(2021, 4, 1, 12, 33, 41)
        print(f"Date: {date.strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        for product, quantity in cart.items():
            print(f"{quantity} {product}s "
                  f"for {quantity * self.products[product]} dollars")
        total = self.total_product_price(cart)
        print(f"Total cost is {total} dollars\n"
              f"See you again!\n")
        return total
