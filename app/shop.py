class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 provided_products: dict) -> None:
        self.name = name
        self.location = location
        self.provided_products = provided_products
