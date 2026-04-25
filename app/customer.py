import json
import os


config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path, "r") as f:
    data = json.load(f)

customers_lists = data["customers"]
customers_dicts = {key: info for key, info in enumerate(customers_lists)}
product_carts = {i: value["product_cart"] for i, value in customers_dicts.items()}


if __name__ == "__main__":
    print(product_carts)
