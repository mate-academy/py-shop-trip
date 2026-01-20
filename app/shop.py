class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            product_prices: dict
    ) -> None:
        self.name = name
        self.location = location
        self.product_prices = product_prices
