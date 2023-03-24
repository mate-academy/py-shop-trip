class Shop:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int, int],
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
