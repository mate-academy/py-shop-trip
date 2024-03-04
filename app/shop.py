class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            product_cart: dict
    ) -> None:
        self.name = name
        self.location = location
        self.product_cart = product_cart


def create_shops(configs: dict) -> list[Shop]:
    shops = []
    for shop in configs["shops"]:
        shop = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        shops.append(shop)

    return shops
