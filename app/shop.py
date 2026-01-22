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
        shop_pos_x = self.location[0]
        shop_pos_y = self.location[1]
        customer_pos_x = customer.location[0]
        customer_pos_y = customer.location[1]
        return sqrt(
            (shop_pos_x - customer_pos_x) ** 2
            + (shop_pos_y - customer_pos_y) ** 2
        )

    def shopping_cost(self, customer: Customer) -> int | float:
        total_price = 0
        for product, amount in customer.product_cart.items():
            total_price += self.products.get(product) * amount
        return total_price

    def issue_receipt(self, customer: Customer) -> None:
        date = datetime.datetime.now()
        print(f'\nDate: {date.strftime("%d/%m/%Y %H:%M:%S")}\n'
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")
        for product, count in customer.product_cart.items():
            cost = self.products[product] * count
            print(f"{count} {product}s for "
                  f"{int(cost) if float(cost) == int(cost) else cost} dollars")
        print(
            f"Total cost is {self.shopping_cost(customer)} dollars\n"
            f"See you again!"
        )
