class Shop:
    def __init__(self, store_name: str,
                 location: list,
                 products: dict) -> None:
        self.store = store_name
        self.location = location
        self.products = products
