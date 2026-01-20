class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]
