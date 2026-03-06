import datetime

from app.customer import Customer


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def get_products_cost(self, cart: dict) -> float:
        return sum(count * self.products[item] for item, count in cart.items())

    def print_receipt(self, customer: Customer, total_cost: float) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product_name, count in customer.product_cart.items():
            price_per_unit = self.products[product_name]
            total_for_product = count * price_per_unit
            print(f"{count} {product_name}s for {total_for_product:g} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
