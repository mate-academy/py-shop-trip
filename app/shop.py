class Shop:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int, int],
    ) -> None:
        self._name = name
        self.products = products
        self.location = location

    @property
    def name(self) -> str:
        return self._name
