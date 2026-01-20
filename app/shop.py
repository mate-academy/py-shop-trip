class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def shop_create_list(config_file: dict) -> list[Shop]:

    shops_list = []

    for shop_attributes in config_file["shops"]:
        shop_obj = Shop(**shop_attributes)
        shops_list.append(shop_obj)

    return shops_list
