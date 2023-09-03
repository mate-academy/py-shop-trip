import json
from typing import Union


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.cost_of_milk = products["milk"]
        self.cost_of_bread = products["bread"]
        self.cost_of_butter = products["butter"]

    @classmethod
    def from_json(cls, json_string: Union[str, bytes]) -> object:
        json_dict = json.loads(json_string)
        return cls(**json_dict)


def shop_list() -> list:
    shops_list = []
    with open(
            "config.json", "r"
    ) as json_file:
        shops_data = json.loads(json_file.read())
        for shop in shops_data["shops"]:
            shops_list.append(Shop(**shop))
    return shops_list
