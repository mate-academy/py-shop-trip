import os
import json


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")
location_shop1 = {}


class Shop:
    def __init__(self, content: dict) -> list:
        self.content = content

    def shop1_location_shop1() -> dict:
        with open(relative_path, "r") as file:
            content = json.load(file)
        shops = content.get("shops")
        location_shop1 = {}
        for elem_ in shops:
            name = elem_.get("name")
            location_shop = elem_.get("location")
            location_shop1.update({name: location_shop})
        return location_shop1
