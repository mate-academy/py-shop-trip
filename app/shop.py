import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self, shop_data: dict) -> None:
        self.name = shop_data["name"]
        self.location = shop_data["location"]
        self.products = shop_data["products"]

    def calculate_products_cost(self, customer: Customer) -> int | float:
        total_price = 0
        for product, amount in customer.product_cart.items():
            product_cost = amount * self.products[product]
            total_price += product_cost

        return total_price

    def print_receipt(self, customer: Customer) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"Date: {current_time}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"
        )

        for product, amount in customer.product_cart.items():
            product_cost = amount * self.products[product]
            print(
                f"{amount} {product}s for {product_cost:g} dollars"
            )

        total_cost = self.calculate_products_cost(customer)

        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )
