class Shop:
    def __init__(
            self, name: str,
            location: list[int],
            products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(
            self, product_cart: dict) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            total_cost += quantity * self.products.get(product, 0)
        return total_cost
