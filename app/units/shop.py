from dataclasses import dataclass, asdict

from app.units.location import Location
from app.units.showcase import Showcase
from app.units.product_cart import ProductCart


@dataclass
class Shop:
    name: str
    location: Location
    products: Showcase

    def purchase(self, customer_name: str, cart: ProductCart) -> float:
        print(
            "Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            "You have bought: "
        )
        total_cost = 0
        for article, quantity in asdict(cart).items():
            amount = self.calculate_purchases(quantity, article)
            print(f"{quantity} {article}s for {amount} dollars")
            total_cost += amount
        print(
            f"Total cost is {total_cost} dollars\n"
            "See you again!\n"
        )
        return total_cost

    def calculate_purchases(self, quantity: int, article: str) -> float:
        return quantity * getattr(self.products, article)
