class Shop:
    def __init__(self, data_shop: dict) -> None:
        self.name = data_shop["name"]
        self.location = data_shop["location"]
        self.product = data_shop["products"]
