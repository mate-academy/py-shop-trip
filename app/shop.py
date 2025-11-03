from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Shop:
    name: str
    location: List[float]
    products: Dict[str, float]

    def calculate_cart_cost(self, cart: Dict[str, int]) -> float:
        """
        Calculate the total cost of the cart.
        """
        total_cost = 0
        for product, quantity in cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
        return total_cost

    def print_check(self, customer_name: str, cart: Dict[str, int]) -> None:
        """
        Print the check for the cart.
        """

        print(f"Thanks, {customer_name}, for your purchase!"),
        print("You have bought:"),

        # produkty z koszyka
        for product, quantity in cart.items():
            if product in self.products:
                price = self.products[product] * quantity
                price_str = int(price) if price == int(price) else price
                print(f"{quantity} {product}s for {price_str} dollars")

        # suma całkowita
        total_cost = self.calculate_cart_cost(cart)
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
