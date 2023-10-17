from typing import List, Dict, Union
from app.customer import convert_file
import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, Union[int, float]]


def create_shops() -> List[Shop]:
    markets = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    ) for shop in convert_file()["shops"]]

    return markets
