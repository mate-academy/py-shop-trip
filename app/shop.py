from typing import Dict
from math import sqrt
import datetime
from dataclasses import dataclass  

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: Dict[str, float]

    def calculate_trip_distance(self, customer: "Customer") -> float:
        shop_x, shop_y = self.location
        customer_x, customer_y = customer.location
        return sqrt((shop_x - customer_x) ** 2 + (shop_y - customer_y) ** 2)

    def shopping_cost(self, customer: Customer) -> float:

        total_price = 0
        for product, amount in customer.product_cart.items():
            total_price += self.products.get(product, 0) * amount
        return total_price

    def issue_receipt(self, customer: "Customer") -> None:
        date = datetime.datetime.now()
        print(f'\nDate: {date.strftime("%d/%m/%Y %H:%M:%S")}'
              f"\nThanks, {customer.name}, for your purchase!"
              "\nYou have bought:")
        for product, amount in customer.product_cart.items():
            cost = self.products[product] * amount
            print(
                f"{amount} {product}s for "
                f"{int(cost) if float(cost) == int(cost) else cost} dollars"
            )
        print(
            f"Total cost is {self.shopping_cost(customer)} "
            f"dollars\nSee you again!"
        )
