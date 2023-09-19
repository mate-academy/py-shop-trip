from typing import Dict, Any
import datetime


class Shop:
    def __init__(self, info: Dict[str, Any]) -> None:
        self.name = info["name"]
        self.location = info["location"]
        self.products = info["products"]

    def check_printing(self, customer: object) -> None:
        from app.customer import Customer
        assert isinstance(customer, Customer)
        current = datetime.datetime.now()
        timestamp = f"Date: {current.strftime('%d/%m/%Y %H:%M:%S')}"

        print(f"\n{timestamp}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, amount in customer.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{amount * self.products[product]} dollars")
        print(f"Total cost is "
              f"{customer.calculate_products_cost(self)} dollars")
        print("See you again!\n")
