import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost(self, cart: dict) -> float:
        return sum(
            self.products[product] * amount
            for product, amount in cart.items()
        )

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        print()
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total = 0

        for product, amount in cart.items():
            price = self.products[product]
            cost = price * amount
            total += cost
            print(f"{amount} {product}s for {cost:g} dollars")

        print(f"Total cost is {total} dollars")
        print("See you again!")
        print()
