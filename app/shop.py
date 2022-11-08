import dataclasses
from datetime import datetime
from typing import List


@dataclasses.dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def calculate_price_for_cart(self, product_cart: dict):
        return sum(self.products[product] * quantity
                   for product, quantity in product_cart.items())

    def sell_products(self, customer):
        # print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        fake_date = datetime(2021, 1, 4, 12, 33, 41)
        print(f"Date: {fake_date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        total_price = 0
        for product, quantity in customer.product_cart.items():
            total_price += self.sell_product(product, quantity)
        print(f"Total cost is {total_price} dollars")
        customer.money -= total_price
        print("See you again!\n")

    def sell_product(self, product, quantity):
        price = self.products[product] * quantity
        print(f"{quantity} {product}s for {price} dollars")
        return price
