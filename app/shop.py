from app.parse_all import ParseJsonMixin


class Shop(ParseJsonMixin):
    all_shops = []

    def __init__(
            self,
            name: str = None,
            location: list[int] = None,
            products: dict = None
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.all_shops.append(self)
