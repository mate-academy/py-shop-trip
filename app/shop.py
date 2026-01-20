from typing import List


class Shop:
    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_product_cart_price(self, product_cart: dict) -> dict:
        if not all(
            [product in self.products for product in product_cart]
        ):
            return
        recipe = {
            (
                f"{amount} {product}s for "
                f"{self.products[product] * amount} dollars"
            ): (self.products[product] * amount)
            for product, amount in product_cart.items()
        }
        return {"recipe": recipe, "price": sum(recipe.values())}
