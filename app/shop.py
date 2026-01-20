class Shop:

    instances = []

    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int]
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.__class__.instances.append(self)
