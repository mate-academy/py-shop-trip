class Shop:
    def __init__(
            self,
            shop: dict
    ) -> None:
        self._name: str = shop["name"]
        self._location: list[int] = shop["location"]
        self._products: dict[str, int] = shop["products"]

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> list[int]:
        return self._location

    @property
    def products(self) -> dict[str, int]:
        return self._products
