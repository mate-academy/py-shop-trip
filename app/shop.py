import datetime
from dataclasses import dataclass
from typing import Any

from app.coordinates import Coordinates


@dataclass
class Shop:
    name: str
    location: Coordinates
    products: dict[str, float] = None

    def __post_init__(self) -> None:
        if self.products is None:
            self.products = dict()

    @staticmethod
    def from_dict(shop: dict[str, Any]) -> "Shop":
        return Shop(
            name=shop.get("name"),
            location=Coordinates(*shop.get("location")),
            products=shop.get("products")
        )

    def groceries_cost(
            self,
            product_cart: dict[str, int]
    ) -> dict[str, float]:
        return {
            item: quantity * self.products.get(item, 0.0)
            for item, quantity in product_cart.items()
        }

    @staticmethod
    def print_receipt(
            customer_name: str,
            product_cart: dict[str, int],
            receipt: dict[str, float],
            total: float
    ) -> None:
        print("\nDate:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("Thanks, {}, for your purchase!".format(customer_name))
        print("You have bought:")
        for item, quantity in product_cart.items():
            print("{} {}s for {:g} dollars".format(
                quantity, item, receipt.get(item, 0.0))
            )
        print("Total cost is {} dollars\nSee you again!\n".format(total))
