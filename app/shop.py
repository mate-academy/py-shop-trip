import datetime

from app.customer import Customer
from app.utils import clean_round


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def product_cart_cost(self, product_cart: dict) -> dict:
        return {
            product: clean_round(value * self.products[product])
            for product, value in product_cart.items()
        }

    def purchase(self, customer: Customer) -> None:
        product_cost = self.product_cart_cost(customer.product_cart)
        print(
            f"{datetime.datetime.now().strftime('Date: %d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:"
        )
        for product in product_cost:
            print(f"{customer.product_cart[product]} {product}s "
                  f"for {product_cost[product]} dollars")

        print(
            f"Total cost is {clean_round(sum(product_cost.values()))} dollars"
            "\nSee you again!\n"
        )
