from __future__ import annotations
from typing import List
import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def shops_creating(cls, config: dict) -> List[Shop]:
        shops = [
            cls(
                shop["name"],
                shop["location"],
                shop["products"],
            )
            for shop in config["shops"]]

        return shops

    def get_check(self, customer: Customer) -> None:
        total = 0
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\nYou have bought: "
        )
        for product, amount in customer.product_cart.items():
            print(
                f"{amount} {product}s for "
                f"{amount * self.products[product]} dollars"
            )
            total += (amount * self.products[product])

        print(f"Total cost is {total} dollars\nSee you again!\n")
