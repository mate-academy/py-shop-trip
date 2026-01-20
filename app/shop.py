from dataclasses import dataclass
from typing import List
from app.data_initial import data


@dataclass
class Shop:
    name: str
    location: list[int, int]
    product_cost: dict


def shop_initial() -> List[Shop]:
    shops = []
    for idx in range(len(data["shops"])):
        shops.append(
            Shop(
                data["shops"][idx]["name"],
                data["shops"][idx]["location"],
                data["shops"][idx]["products"]
            )
        )
    return shops
