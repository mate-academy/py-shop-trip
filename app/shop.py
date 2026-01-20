class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def has_all_products(self, product_cart: dict) -> bool:
        for product in product_cart:
            if product not in self.products:
                return False
        return True
