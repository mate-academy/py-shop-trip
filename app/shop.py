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

    def get_product_price(self, product: str) -> float:
        return self.products[product]

    def check_product_price(self, product: str) -> float:
        return self.products.get(product)
