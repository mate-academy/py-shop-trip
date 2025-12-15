from math import dist

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance(self, customer: Customer) -> float:
        return dist(self.location, customer.location)

    def print_receipt(self, customer: Customer) -> None:
        print(
            "\nDate: 04/01/2021 12:33:41\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:"
        )
        total_cost = 0
        for product, count in customer.product_cart.items():
            price = self.products[product] * count
            if price == int(price):
                price = int(price)
            print(f"{count} {product}s for {price} dollars")
            total_cost += price
        print(
            f"Total cost is {total_cost} dollars\n"
            "See you again!\n"
        )
