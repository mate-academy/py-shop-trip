# flake8: noqa
from decimal import Decimal
from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int | float],
            products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def buy_products(
            self,
            customer: Customer,
            message: bool = False) -> int | float:
        result = Decimal("0")

        for product_name, amount in customer.product_cart.items():
            if product_name not in self.products:
                continue

            price = Decimal(
                str(amount)
            ) * Decimal(
                str(self.products[product_name])
            )

            if message:
                print(f"{amount} {product_name}s for {int(price) if float(price).is_integer() else price} dollars")

            result += price
        if message:
            print(f"Total cost is {result} dollars")
            print("See you again!")
        return result

    def recit(self, poduct_list: dict) -> None:
        pass
