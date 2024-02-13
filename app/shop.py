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

    def calculate_product_cost(self, product_cart: dict) -> float:
        return sum([self.products[product] * quantity
                    for product, quantity in product_cart.items()
                    if product in self.products])
