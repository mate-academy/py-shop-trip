import datetime

from app.utils import format_money


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

    def calculate_products_cost(self, product_cart: dict) -> float:
        cost = 0.0
        for item, quantity in product_cart.items():
            if item in self.products:
                cost += self.products[item] * quantity
        return cost

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict
    ) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print()
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for item, quantity in product_cart.items():
            if item in self.products:
                cost = self.products[item] * quantity
                print(f"{format_money(quantity)} {item}s "
                      f"for {format_money(cost)} dollars")

        total_cost = self.calculate_products_cost(product_cart)

        print(f"Total cost is {format_money(total_cost)} dollars")
        print("See you again!")
        print()
