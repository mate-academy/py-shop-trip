from typing import List
from dataclasses import dataclass
from app.data_json import load_data


@dataclass
class Shop:
    name: str
    location: List[float]
    products: dict

    @classmethod
    def get_shop(cls) -> list["Shop"]:
        data = load_data(filename="app/config.json")
        shop = [
            cls(
                name=data_shop["name"],
                location=data_shop["location"],
                products=data_shop["products"]
            )
            for data_shop in data["shops"]
        ]
        return shop
