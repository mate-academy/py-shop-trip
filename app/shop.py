import datetime

from dataclasses import dataclass

from app.customer import Customer
from app.product import Product


@dataclass
class Shop:
    name: str
    location: list[int]
    products: list[Product]

    def print_receipt(self, customer: Customer) -> tuple[str, int]:
        cart = ""
        total = 0

        for customer_product in customer.product_cart:
            for product in self.products:
                if customer_product.product_name == product.name:
                    products_cost = (customer_product.product_amount
                                     * product.price)
                    cart += (f"{customer_product.product_amount} "
                             f"{product.name}s for {products_cost} dollars\n")
                    total += customer_product.product_amount * product.price

        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        return (f"Date: {data}\n"
                f"Thanks, {customer.name}, for you purchase!\n"
                f"You have bought: \n"
                f"{cart}"
                f"Total cost is {total} dollars\n"
                f"See you again!"), total
