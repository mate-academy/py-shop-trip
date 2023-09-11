class Shop:
    def __init__(self, info: dict) -> None:
        self.location = info["location"]
        self.products = info["products"]
