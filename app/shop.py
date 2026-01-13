class Shop:
    def __init__(self,
                 name: str,
                 location: list[int, int],
                 products: dict[str, int]) -> None:
        self.name = name
        self.location = location
        self.products = products


def create_shop_from_list(shops_list: list[dict]) -> list[Shop]:
    shops = []
    for shop in shops_list:
        shops.append(Shop(shop["name"],
                          shop["location"],
                          shop["products"]))

    return shops
