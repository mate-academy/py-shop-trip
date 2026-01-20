from __future__ import annotations

from app.location import Location


class Shop:
    def __init__(
            self,
            name: str,
            location: Location,
            products: dict[str, int | float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def total_cost_of(self, products_to_buy: dict[str, int | float]) -> float:
        total_cost = 0
        for product, amount in products_to_buy.items():
            if product not in self.products:
                raise KeyError(
                    f"Product {product} is not available at {self.name}"
                )
            total_cost += amount * self.products[product]

        return total_cost

    @classmethod
    def from_dict(cls, shop: dict) -> Shop:
        return cls(
            name=shop.get("name"),
            location=Location(shop.get("location")),
            products=shop.get("products")
        )
