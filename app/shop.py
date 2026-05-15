import datetime
from decimal import Decimal

from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: tuple,
        products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_shopping(self, product_cart: dict) -> Decimal:
        cost = Decimal("0.0")
        for product in product_cart:
            cost += (
                Decimal(str(product_cart.get(product, 0.0)))
                * Decimal(str(self.products.get(product, 0.0)))
            )
        return cost

    def shopping(self, customer: Customer) -> Decimal:
        formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = Decimal("0.0")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product in customer.product_cart:
            product_qty = Decimal(
                str(
                    customer.product_cart.get(product, 0.0)
                )
            )
            product_unit_price = Decimal(
                str(
                    self.products.get(product, 0.0)
                )
            )
            cost = Decimal(str(product_qty * product_unit_price))
            print(
                f"{product_qty.normalize()} {product}s for "
                f"{round(cost, 2).normalize()} dollars"
            )
            total_cost += cost

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

        return total_cost
