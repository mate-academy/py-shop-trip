class Shop:
    def __init__(
        self,
        name: str,
        location: list[float],
        products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
