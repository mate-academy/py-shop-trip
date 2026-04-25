import os
import json


config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path, "r") as f:
    data = json.load(f)


shop_lists = data["shops"]
shop_dicts = {key: info for key, info in enumerate(shop_lists)}
shop_product_carts = {key: info["products"] for key, info in shop_dicts.items()}


if __name__ == "__main__":
    print(shop_product_carts)