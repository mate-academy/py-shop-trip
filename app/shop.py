class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            product: dict
    ) -> dict:
        self.name = name
        self.location = location
        self.product = product
