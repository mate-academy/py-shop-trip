from app.customer import Customer
from datetime import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def sell_products(self, customer: Customer) -> None:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%m/%d/%Y %H:%M:%S")
        print(formatted_time)
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            product_cost = round(self.products[product] * quantity, 2)
            total_cost += product_cost
            if quantity <= 1:
                print(f"{quantity} {product} for {product_cost} dollars")
            if quantity > 1:
                print(f"{quantity} {product}s for {product_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

    def count_total_price(self, customer: Customer) -> float:
        return round(sum([
            self.products[product] * quantity
            for product, quantity in customer.product_cart.items()
        ]), 2)
