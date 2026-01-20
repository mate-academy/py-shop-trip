import datetime
from decimal import Decimal

from app.location import Location


class Shop:
    def __init__(
        self, name: str,
        location: list[int, int],
        products: dict
    ) -> None:
        self.name = name
        self.location = Location(*location)
        self.products = products

    def prints_receipt(self, product_cart: dict, cust_name: str) -> None:
        purchases_info = ""
        all_products_total = 0

        for product, amount in product_cart.items():
            product_total = amount * Decimal(str(self.products[product]))

            if product_total == product_total.to_integral():
                product_total = product_total.to_integral()

            all_products_total += product_total

            purchases_info += (f"{amount} {product}s "
                               f"for {product_total} dollars\n")

        print(f"Date: "
              f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
              f"Thanks, {cust_name}, for your purchase!\n"
              "You have bought:\n"
              f"{purchases_info}"
              f"Total cost is {all_products_total} dollars\n"
              "See you again!\n")
