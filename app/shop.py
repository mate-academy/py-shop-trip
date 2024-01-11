import datetime
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer


class Shop:
    def __init__(self, name: str, location: List, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_purchase_cost(self, customer: "Customer") -> float:
        total_cost = sum(
            self.products[product] * quantity for product,
            quantity in customer.product_cart.items()
            if product in self.products)
        return round(total_cost, 2)

    def print_receipt(self, customer: "Customer") -> None:
        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}\nThanks, "
              f"{customer.name}, "
              f"for your purchase!\nYou have bought:")
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_price = self.products[product]
                cost_for_product = product_price * quantity
                if (isinstance(cost_for_product, float)
                        and cost_for_product.is_integer()):
                    cost_for_product = int(cost_for_product)
                print(f"{quantity} {product}s for {cost_for_product} dollars")
        total_cost = self.calculate_purchase_cost(customer)
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
