class Shop:

    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self):
        return f"Name: {self.name}"
