from datetime import datetime


class Shop:
    """Represents a shop and its product prices."""

    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def count_prices(self,
                     customer_cart: dict[str, float]) -> float:
        """Calculate total price for customer's cart."""
        total = 0
        for prod, qty in customer_cart.items():
            total += self.products[prod] * qty
        return total

    def make_purchase(self,
                      name: str,
                      product_cart: dict[str, float]) -> None:
        """Print receipt for customer's purchase."""
        total_price = self.count_prices(product_cart)

        date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {date}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought: ")

        for prod, qty in product_cart.items():
            cost = self.products[prod] * qty
            if cost == int(cost):
                cost = int(cost)
            print(f"{qty} {prod}s for {cost} dollars")

        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")
