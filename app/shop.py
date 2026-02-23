class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products_available: dict) -> None:
        self.name = name
        self.location = location
        self.products_available = products_available
