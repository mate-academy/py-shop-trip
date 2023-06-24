from app.customer import customer_create_list, customer_calculations, receipts
from app.shop import shop_create_list
from app.car import gas_trip_cost
import json


def shop_trip() -> None:
    with open(
            "app/config.json"
    ) as f:
        config_file = json.load(f)
    shops = shop_create_list(config_file)
    customers = customer_create_list(config_file, shops)
    gas_trip_cost(customers, shops, config_file)
    customer_calculations(customers, shops)
    receipts(customers, shops)
