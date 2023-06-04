class Shop:
    def __init__(self, dictionary: dict) -> None:
        self.name = dictionary["name"]  # str
        self.location = dictionary["location"]  # list
        self.products = dictionary["products"]  # dict
