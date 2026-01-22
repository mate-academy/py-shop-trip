from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_products_cost(self, cart: dict) -> float:
        if not self.has_all_products(cart):
            raise ValueError("Not all products available in shop")
        return sum(self.products[item] * cart[item] for item in cart)

    def has_all_products(self, cart: dict) -> bool:
        return all(item in self.products for item in cart)
