class Shop:
    def __init__(self, config: {}) -> None:
        self.name = config["name"]
        self.location = config["location"]
        self.products = config["products"]
