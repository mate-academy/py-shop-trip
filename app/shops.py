from app.data import shop_list


class Shop:
    def __init__(self, name, loc, prices):
        self.name = name
        self.loc = loc
        self.prices = prices


shops = [
    Shop(
        shop["name"],
        shop["location"],
        list(shop["products"].values())
    )
    for shop in shop_list
]
