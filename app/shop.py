import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, float]

    def calculate_products_cost(
        self,
        product_cart: dict[str, int]
    ) -> float:
        """Calculate total cost of the customer's cart in this shop."""
        return sum(
            self.products[product] * amount
            for product, amount in product_cart.items()
        )

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int]
    ) -> None:
        """Print the purchase receipt using the current time."""
        print(f"\nDate: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")

        for product, amount in product_cart.items():
            cost = self.products[product] * amount
            print(f"{amount} {product}s for {round(cost, 2)} dollars")

        total_cost = self.calculate_products_cost(product_cart)
        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!\n")
