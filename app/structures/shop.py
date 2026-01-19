from app.structures.coords import Coords


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = Coords(*location)
        self.products = products
