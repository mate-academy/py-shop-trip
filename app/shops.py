class Shop:
    def __init__(self, shops_dict: dict) -> None:
        self.name = shops_dict["name"]
        self.location = shops_dict["location"]
        self.products = shops_dict["products"]
