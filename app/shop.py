import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: str,
            products: str
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, cart: float) -> float:
        return sum(
            self.products[prod] * qty
            for prod, qty in cart.items()
        )

    def print_receipt(
            self, customer: str,
            cart: float, total_cost: float
    ) -> str:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for prod, qty in cart.items():
            price = self.products[prod] * qty
            price = str(price).rstrip("0").rstrip(".")
            print(f"{qty} {prod}s for {price} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
