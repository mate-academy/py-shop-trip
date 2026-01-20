import json
import os


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def calculate_money_for_shop() -> list:
    all_costs = []
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "config.json")
    with open(path, "r") as f:
        shop_part = json.load(f)

    customers = shop_part["customers"]
    shops = shop_part["shops"]

    for customer in customers:
        for shop in shops:
            total = 0
            for product_name, amount in customer["product_cart"].items():
                price = shop["products"].get(product_name)
                total += price * amount
            all_costs.append(total)
    return all_costs
