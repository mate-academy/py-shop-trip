import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, cart: dict) -> float:
        total = 0
        now = datetime.datetime.now()
        print(f'\nDate: {now.strftime("%d/%m/%Y %H:%M:%S")}')  # noqa
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in cart.items():
            if product in self.products:
                cost = self.products[product] * quantity
                total += cost
                cost_str = f"{cost:.2f}".rstrip("0").rstrip(".")  # noqa: E231
                print(f"{quantity} {product}s for {cost_str} dollars")
        total_str = f"{total:.2f}".rstrip("0").rstrip(".")  # noqa: E231
        print(f"Total cost is {total_str} dollars")
        print("See you again!\n")
        return total
