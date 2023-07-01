class Shop:
    shop_list = []

    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shop_list.append(self)

    def __str__(self) -> str:
        return self.name
