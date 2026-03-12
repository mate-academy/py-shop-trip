import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, cart: dict) -> float:
        total = 0

        print(
            "\nDate: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, amount in cart.items():
            price = self.products[product]
            cost = price * amount
            total += cost
            print(f"{amount} {product}s for {cost:g} dollars")

        print(f"Total cost is {total:g} dollars")
        print("See you again!")
        print()

        return total
