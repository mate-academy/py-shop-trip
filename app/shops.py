from app.data import shops_list


class Shop:
    def __init__(self, name, location, prices):
        self.name = name
        self.location = location
        self.prices = prices


shops = [
    Shop(
        shop["name"],
        shop["location"],
        list(shop["products"].values())
    )
    for shop in shops_list
]
