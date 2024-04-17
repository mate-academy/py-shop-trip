from app.location import Location


class Shop:
    def __init__(
        self,
        name: str,
        location: Location,
        products: dict,
    ) -> None:
        self._name = name
        self._products = products
        self._location = location

    @property
    def name(self) -> str:
        return self._name

    @property
    def products(self) -> dict:
        return self._products

    @property
    def location(self) -> Location:
        return self._location
