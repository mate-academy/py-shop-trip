import datetime
import math
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance(self, other: list) -> float:
        distance = (math.sqrt((other[0] - self.location[0])
                              ** 2 + (other[1] - self.location[1]) ** 2))
        return distance

    def calculate_total_price(self, other: dict) -> float:
        result = [self.products[product] * other[product] for
                  product in self.products.keys()]
        return sum(result)

    def print_purchased_products(self, customer: "Customer") -> None:
        time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total = 0.0
        for key, value in self.products.items():
            total_price = float(value * customer.products[key])
            total += total_price
            print(f"{customer.products[key]} {key}s for "
                  f"{total_price:g} dollars")
        total = round(total, 2)
        print(f"Total cost is {total:g} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
