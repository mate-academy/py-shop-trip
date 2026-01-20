from math import dist


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def distance(self, other_location: list) -> float:
        return dist(self.location, other_location)
