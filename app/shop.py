from typing import Any
import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def format_price(self, price: float | int) -> str | int:
        rounded_price = round(float(price), 2)

        if rounded_price.is_integer():
            return int(rounded_price)
        else:
            rounded_price = round(rounded_price, 1)
            return f"{rounded_price}"

    def calculate_bought_price(self, product: str, count: int) -> float:
        return self.products.get(product) * count

    def buy_products_cost(self, **kwargs) -> float:
        total_cost = 0
        for name, count in kwargs.items():
            total_cost += self.calculate_bought_price(name, count)
        return total_cost

    def print_bill(self, customer: Any) -> None:
        current_time = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        total = 0
        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, count in customer.product_cart.items():
            cost = self.calculate_bought_price(product, count)
            total += cost
            cost = self.format_price(cost)
            print(f"{count} {product}s for {cost} dollars")
        total = round(total, 2)
        print(f"Total cost is {total} dollars")

        print("See you again!")
