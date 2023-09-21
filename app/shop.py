from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def purchase_amount(self, product_cart: dict) -> float:
        return sum(
            amount * float(product_cart[product])
            for product, amount in self.products.items()
        )
