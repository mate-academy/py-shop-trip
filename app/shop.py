class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 available_products: dict[str, float]
                 ) -> None:
        self.name = name
        self.location = location
        self.available_products = available_products
