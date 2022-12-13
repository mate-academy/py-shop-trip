class Shop:
    def __int__(
            self,
            name: str,
            location: list,
            products_provides: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products_provides = products_provides
