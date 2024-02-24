class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def from_dict(shop_list: list) -> list:
        new_list = []
        for shop in shop_list:
            new_list.append(Shop(name=shop["name"],
                                 location=shop["location"],
                                 products=shop["products"],))
        return new_list
