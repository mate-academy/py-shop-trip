class Shop:
    def __init__(self, info_dict: dict) -> None:
        self.name = info_dict["name"]
        self.location = info_dict["location"]
        self.products = info_dict["products"]
