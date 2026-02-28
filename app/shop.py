class Shop:
    def __init__(self, name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase(self, product_cart: dict) -> dict:
        need_return = {}
        for product, count in product_cart.items():
            if product in self.products:
                need_return[product] = self.products[product] * count
        return need_return
