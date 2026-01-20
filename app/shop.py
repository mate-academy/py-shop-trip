class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_product_price(self, product_name: str) -> int:
        if product_name in self.products:
            return self.products[product_name]
        else:
            raise ValueError(f"{product_name} is not sold in {self.name}")
