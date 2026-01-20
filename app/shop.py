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

    def get_item_price(self, item: str) -> float:
        return self.products[item]

    def check_item_price(self, item: str) -> float:
        return self.products.get(item)
