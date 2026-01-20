import datetime
from dataclasses import dataclass
from math import sqrt

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_trip_distance(self, customer: Customer) -> int | float:
        shop_x = self.location[0]
        shop_y = self.location[1]
        customer_x = customer.location[0]
        customer_y = customer.location[1]
        return sqrt((shop_x - customer_x) ** 2 + (shop_y - customer_y) ** 2)

    def shopping_cost(self, customer: Customer) -> int | float:
        total_price = 0
        for product, amount in customer.product_cart.items():
            total_price += self.products.get(product) * amount
        return total_price

    def issue_receipt(self, customer: Customer) -> None:
        date = datetime.datetime.now()
        print(f'\nDate: {date.strftime("%d/%m/%Y %H:%M:%S")}'
              f"\nThanks, {customer.name}, for your purchase!"
              f"\nYou have bought:")  # noqa: E231
        for product, amount in customer.product_cart.items():
            cost = self.products[product] * amount
            print(f"{amount} {product}s for "
                  f"{int(cost) if float(cost) == int(cost) else cost} dollars")
        print(
            f"Total cost is {self.shopping_cost(customer)} dollars"
            f"\nSee you again!"
        )
