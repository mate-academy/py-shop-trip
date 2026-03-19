import datetime

from app.customer import Customer


class Shop:
    def __init__(self, shop_data: dict) -> None:
        self.name = shop_data["name"]
        self.location = shop_data["location"]
        self.products = shop_data["products"]

    def find_shopping_cost(self, customer: Customer) -> float:
        shopping_cost = sum(
            customer.product_cart[product] * self.products[product]
            for product in customer.product_cart
        )
        return shopping_cost

    def print_receipt(self, customer: Customer) -> None:
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"
        )
        shopping_cost = self.find_shopping_cost(customer)
        for key, value in customer.product_cart.items():
            product_cost = value * self.products[key]
            if product_cost % 1 == 0:
                product_cost = int(product_cost)
            print(
                f"{value} {key}s for "
                f"{product_cost} dollars"
            )
        print(
            f"Total cost is {shopping_cost} dollars\n"
            f"See you again!\n"
        )
