from datetime import datetime
from app.calculate_distance import calculate_distance
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance_to_customer(self, customer: Customer) -> float:
        distance = calculate_distance(self.location, customer.location)
        return distance

    def calculate_purchase_cost(self, customer: Customer) -> int | float:
        return sum(quantity * customer.product_cart[item]
                   for item, quantity in self.products.items())

    def print_rides_to_shop(self, customer: Customer) -> None:
        print(f"{customer.name} rides to {self.name}\n")

    @staticmethod
    def round_num(num: int | float) -> int | float:

        float_num = float(round(num, 2))

        return int(float_num) if float_num.is_integer() else float_num

    def print_receipt(self, customer: Customer) -> None:
        total_amount = 0
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for item, quantity in customer.product_cart.items():
            if item in self.products:
                cost = quantity * self.products[item]
                total_amount += cost
                print(f"{quantity} {item}s for {self.round_num(cost)} dollars")
        print(f"Total cost is {total_amount} dollars")
        print("See you again!")
