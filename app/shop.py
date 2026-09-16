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

    def calculate_products_cost(self, cart: dict[str, int]) -> float:
        total = 0.0
        for product, quantity in cart.items():
            if product in self.products:
                total += self.products[product] * quantity
        return total

    def print_receipt(
        self,
        customer_name: str,
        cart: dict[str, int],
        total_cost: float
    ) -> None:
        current_time = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        print()
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in cart.items():
            product_cost = self.products[product] * quantity
            print(
                f"{quantity} {product}s for "
                f"{product_cost:g} dollars"
            )

        print(f"Total cost is {total_cost:g} dollars")
        print("See you again!")
        print()
