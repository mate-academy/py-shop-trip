class Shop:
    def __init__(
            self,
            name: str,
            location: list[int, int],
            products: dict[str, int | float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
