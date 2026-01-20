class Shop:
    def __init__(self, information: dict) -> None:
        self.name = information["name"]
        self.location = information["location"]
        self.products = information["products"]
