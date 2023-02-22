from typing import List

from app.shops.shop import Shop


def creating_shops_classes(shops: List[dict]) -> List[Shop]:
    classes_shop = []
    for shop in shops:
        classes_shop.append(
            Shop(
                name=shop["name"],
                products=shop["products"],
                location=shop["location"],
            )
        )
    return classes_shop
