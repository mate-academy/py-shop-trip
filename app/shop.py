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

    def calculate_total_price(self, num_of_products: list) -> float:
        product_price = [dollar for dollar in self.products.values()]
        result = [num1 * num2 for num1, num2 in
                  zip(product_price, num_of_products)]
        return sum(result)

    def print_purchased_products(self, customer: "Customer") -> None:
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        num_of_products = customer.list_of_products()
        i = 0
        total = 0.0
        for key, value in self.products.items():
            total_price = float(value * num_of_products[i])
            total += total_price
            print(f"{num_of_products[i]} {key}s for {total_price:g} dollars")
            i += 1
        total = round(total, 2)
        print(f"Total cost is {total:g} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
