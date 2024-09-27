class Shop:
    def __init__(self, dictionary: dict) -> None:
        self.name = dictionary.get("name")  # str
        self.location = dictionary.get("location")  # list
        self.products = dictionary.get("products")  # dict
