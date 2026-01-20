import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Shop:
    name: str
    location: list
    products: dict


def create_shop(shops_data: dict) -> Shop | None:
    try:
        shop = Shop(
            name=shops_data["name"],
            location=shops_data["location"],
            products=shops_data["products"]
        )
        return shop
    except KeyError as e:
        print(f"Error: a required field is missing {e}")
        return None
    except ValueError as e:
        print(f"Validation error {e}")
        return None


def load_shops_from_config() -> list[Shop]:
    config_path = Path(__file__).parent / "config.json"
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            shops = []

            if "shops" in config:
                for shop_data in config["shops"]:
                    shop = create_shop(shop_data)
                    if shop:
                        shops.append(shop)

            return shops

    except FileNotFoundError:
        print("No config.json file found")
        return []
    except json.decoder.JSONDecodeError:
        print("Decoding error JSON")
        return []
