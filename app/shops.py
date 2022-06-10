import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict


path = Path(__file__).resolve().parent
with open(path / "config.json", "r") as file:
    config = json.load(file)
    shops = [Shop(**shop) for shop in config["shops"]]
