from app.customer import Customer

from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_product(self, customer: Customer) -> int:
        return sum(self.products[product] * value
                   for product, value in customer.product_cart.items())
