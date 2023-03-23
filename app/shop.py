class Shop:
    def __init__(
            self,
            name: str,
            products: list,
            location: dict,
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
