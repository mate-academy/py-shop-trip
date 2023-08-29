from app.customer import Customer
import datetime


class Shop:
    def __init__(self, name: str, location: list, provided_prod: dict) -> None:
        self.name = name
        self.location = location
        self.provided_prod = provided_prod

    def price_of_products(self, customer: Customer) -> float:
        total_cost = 0
        for key, value in customer.desired_products.items():
            total_cost += value * self.provided_prod[key]
        return total_cost

    def print_receipt(self, customer: Customer) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for product, needed in customer.desired_products.items():
            print(f"{needed} {product}s for "
                  f"{needed * self.provided_prod[product]} dollars")
        print(f"Total cost is {self.price_of_products(customer)} dollars")
        print("See you again!\n")
