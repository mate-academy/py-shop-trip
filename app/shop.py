from dataclasses import dataclass
from app.customer import Customer
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def cost_of_products(self, customer: Customer) -> int:
        total_cost = 0
        for product, num in customer.product_cart.items():
            cost = self.products[product] * num
            total_cost += cost
        return total_cost

    def purchase_receipt(self, customer: Customer) -> int:
        current_date = datetime.datetime.now()
        print(f"Date: {current_date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for product, num in customer.product_cart.items():
            cost = self.products[product] * num
            print(f"{num} {product}s for {cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        return total_cost
