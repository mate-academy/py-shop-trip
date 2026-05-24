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

    def get_products_cost(self, product_cart: dict) -> float:
        total_cost = 0.0

        for product, quantity in product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity

        return total_cost
