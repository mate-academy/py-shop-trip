from datetime import datetime


class Shop:

    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_check(self, name: str, cart: dict) -> None:
        total_costs = 0
        test_date = datetime(2021, 1, 4, 12, 33, 41)
        print(f"Date: {test_date.strftime("%d/%m/%Y %H:%M:%S")}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        for product, amount in cart.items():
            cost = amount * self.products[product]
            print(f"{amount} {product}s for {cost} dollars".replace(".0", ""))
            total_costs += cost
        print(f"Total cost is {total_costs} dollars")
        print("See you again!\n")
