import math


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products


def create_shops(file_name: str) -> list[object]:

    shops = []

    for shop in file_name["shops"]:
        products = {}

        for name_product, value_product in shop["products"].items():
            products[name_product] = value_product

        shop_object = Shop(shop["name"], shop["location"], products)
        shops.append(shop_object)

    return shops


def distance(point_1: list[int], point_2: list[int]) -> float:
    x_axis = point_1[0] - point_2[0]
    y_axis = point_1[1] - point_2[1]
    results = math.sqrt((x_axis**2) + (y_axis**2))
    return results
