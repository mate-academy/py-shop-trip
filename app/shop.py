class Shop:
    def __init__(
            self,
            element: dict,
            name: str,
            location: list,
            product: dict
    ) -> dict:
        self.element = element
        self.name = name
        self.location = location
        self.product = product
