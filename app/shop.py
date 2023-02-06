from math import sqrt


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def distance_calculation(self, other: list) -> float:
        distance = sqrt(
            (self.location[0] - other[0]) ** 2
            + (self.location[1] - other[1]) ** 2
        )
        return round(distance * 2, 2)
