import dataclasses
import json


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    @staticmethod
    def create_shops(json_file: str) -> list:
        with open(json_file, "r") as f:
            data = json.load(f)
            return [Shop(**shop_data) for shop_data in data["shops"]]
