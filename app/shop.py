import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, cart: dict) -> int | float:
        total = 0
        for item, qty in cart.items():
            if item in self.products:
                total += self.products[item] * qty
        return total

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        now = datetime.datetime.now()
        print(f"\nDate: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for item, qty in cart.items():
            price = self.products[item] * qty
            price_str = f"{int(price)}" if price == int(price) else f"{price}"
            print(f"{qty} {item}s for {price_str} dollars")
        total = self.calculate_cart_cost(cart)
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
