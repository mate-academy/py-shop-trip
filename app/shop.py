from datetime import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, cart: dict) -> float:
        total = 0
        for product, quantity in cart.items():
            if product not in self.products:
                return float("inf")  # shop doesn't have product
            total += self.products[product] * quantity
        return total

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        now = datetime(2021, 4, 1, 12, 33, 41)
        print(f"Date: {now.strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total = 0
        for product, quantity in cart.items():
            price = self.products[product] * quantity
            total += price
            if price.is_integer():
                price = int(price)
            print(f"{quantity} {product}s for {price} dollars")

        print(f"Total cost is {total} dollars")
        print("See you again!\n")
