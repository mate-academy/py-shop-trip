import math

from app.config_loader import load_config
from app.shop import shop_dicts


data = load_config()

customers_lists = data["customers"]
customers_dicts = {key: info for key, info in enumerate(customers_lists)}

customers_cars = {
    i: value["car"]
    for i, value in customers_dicts.items()
}

fuel_price = data["FUEL_PRICE"]


def navigator(customer_key: int, shop_key: int) -> float:
    customer_location = customers_dicts[customer_key]["location"]
    shop_location = shop_dicts[shop_key]["location"]

    return math.sqrt(
        (shop_location[0] - customer_location[0]) ** 2
        + (shop_location[1] - customer_location[1]) ** 2
    )
