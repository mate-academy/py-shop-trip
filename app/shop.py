import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, cart: dict[str, int]) -> float:
        return sum(
            self.products[prod] * qty
            for prod, qty in cart.items()
        )

    def print_receipt(
            self,
            customer,
            cart: dict,
            total_cost: float
    ) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for prod, qty in cart.items():
            price =round(self.products[prod] * qty, 2)
            price_str = f"{price:.2f}".rstrip("0").rstrip(".")
            print(f"{qty} {prod}s for {price_str} dollars")

        print(f"Total cost is {total_cost:.2f} dollars")
        print("See you again!\n")
