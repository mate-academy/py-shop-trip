from app.descriptors import ArgsLoader
from app.location import Location


class Shop:
    location = ArgsLoader(Location)

    def __init__(
            self,
            name: str,
            location: Location,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
