class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self) -> str:
        return (f"Shop(name={self.name}, location={self.location}, "
                f"product={self.products})")

    def total_cost_of_product_in_cart(self, product_cart: dict) -> float:
        return sum(
            self.products[key] * value
            for key, value in product_cart.items()
        )
