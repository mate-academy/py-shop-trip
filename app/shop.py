from datetime import datetime

from typing import ForwardRef

Customer = ForwardRef("Customer")


class Product:
    def __init__(self, name: str) -> None:
        self.name = name


class ProductShop(Product):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name)
        self.price = price

    def get_price(self, name: str) -> float:
        if self.name == name:
            return self.price


class ProductCart(Product):
    def __init__(self, name: str, quantity: int) -> None:
        super().__init__(name)
        self.quantity = quantity

    def get_quantity(self, name: str) -> int:
        if self.name == name:
            return self.quantity


class Shop:

    def __init__(self, name: str, location: list,
                 products: list[ProductShop]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_amount_purchase(
            self, customer: Customer, print_check: bool = False
    ) -> float:
        result = 0
        if print_check:
            date_trip = datetime(
                2021, 1, 4, 12, 33, 41
            ).strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {date_trip}\n"
                  f"Thanks, {customer.name}, for your purchase!\n"
                  "You have bought:")
        for each in customer.product_cart:
            for product in self.products:
                if each.name == product.name:
                    quantity = each.get_quantity(each.name)
                    price = product.get_price(each.name)
                    result += quantity * price
                    if print_check:
                        plural = "s" if quantity > 1 else ""
                        amount_each = quantity * price
                        if amount_each % 1 == 0:
                            amount_each = int(amount_each)
                        print(f"{quantity} {product.name}{plural} "
                              f"for {amount_each} dollars")
        if print_check:
            print(f"Total cost is {round(result, 2)} dollars\n"
                  "See you again!\n")
        return round(result, 2)
