from app.customer import Customer
from app.utils import format_price


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: Customer) -> None:
        formatted_time = "04/01/2021 12:33:41"

        print(f"Date: {formatted_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, amount in customer.product_cart.items():
            price = self.products[product]
            cost = round(price * amount, 2)
            total_cost += cost
            print(f"{amount} {product}s for {format_price(cost)} dollars")

        total_cost = round(total_cost, 2)
        print(f"Total cost is {format_price(total_cost)} dollars")
        print("See you again!\n")
