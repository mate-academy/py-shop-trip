from app.utils import format_price


class Shop:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.location: list[float] = data["location"]
        self.products: dict[str, float] = data["products"]

    def has_all_products(self, cart: dict[str, int]) -> bool:
        return all(item in self.products for item in cart)

    def calculate_cart_total(self, cart: dict[str, int]) -> float:

        return sum(
            self.products[item] * quantity
            for item, quantity in cart.items()
        )

    def print_receipt(
            self,
            customer_name: str,
            cart: dict[str, int]
    ) -> None:
        timestamp = "04/01/2021 12:33:41"  # just for tests

        print()
        print(f"Date: {timestamp}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total = 0.0
        for item, quantity in cart.items():
            cost = self.products[item] * quantity
            print(f"{quantity} {item}s for {format_price(cost)} dollars")
            total += cost

        print(f"Total cost is {format_price(total)} dollars")
        print("See you again!\n")
