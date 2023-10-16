from app.data_jason import load_json
import dataclasses
from typing import List


@dataclasses.dataclass
class Stores:
    name: str
    location: List[int]
    products: dict

    @classmethod
    def get_stores(cls) -> list["Stores"]:
        data = load_json(filename="app/config.json")

        stores = []
        for data_store in data["shops"]:
            list_shop = Stores(
                name=data_store["name"],
                location=data_store["location"],
                products=data_store["products"]
            )
            stores.append(list_shop)

        return stores
