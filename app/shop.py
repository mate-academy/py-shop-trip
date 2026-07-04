class Shop:
    def __init__(self, data: dict) -> None:
        self.location = data["location"]
        self.products = data["products"]
        self.name = data["name"]
