class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict,
            fuel: float
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.fuel = fuel
