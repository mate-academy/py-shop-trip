class Shop:
    def __init__(
            self,
            item_dict: dict
    ) -> None:
        self.name = item_dict["name"]
        self.location = item_dict["location"]
        self.products = item_dict["products"]
