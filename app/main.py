import json
from pathlib import Path

from app.customers.creating_customers_classes import creating_customers_classes
from app.data_processing import data_processing
from app.shops.creating_shops_classes import creating_shops_classes


def shop_trip() -> None:
    json_path = Path(__file__).parent.joinpath("config.json")
    with open(json_path, "r") as file_in:
        data = json.load(file_in)

    fuel_price, customers, shops = data.values()
    classes_customers = creating_customers_classes(customers)
    classes_shop = creating_shops_classes(shops)

    data_processing(fuel_price, classes_customers, classes_shop)


if __name__ == "__main__":
    shop_trip()
