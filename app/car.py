import json
import math
import os

from app.shop import shop_dicts


config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path, "r") as f:
    data = json.load(f)

customers_lists = data["customers"]
customers_dicts = {key: info for key, info in enumerate(customers_lists)}
customers_cars = {i: value["car"] for i, value in customers_dicts.items()}
fuel_price = data["FUEL_PRICE"]


def navigator(custumer_key: int, shop_key: int) -> float:
    cl = customers_dicts[custumer_key]["location"]
    sl = shop_dicts[shop_key]["location"]
    return math.sqrt((sl[0] - cl[0])**2 + (sl[1] - cl[1])**2)
