class Shop:
    def __init__(
            self,
            name: str,
            location: list | tuple,
            products: dict
    ) -> None:
        self.name = name
        self.location = list(location)
        self.products = products
