class Shop:
    list_shop = []

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return self.name
