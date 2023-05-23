class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, int]
    ) -> None:

        self.name = name
        self.location = location
        self.products = products
