import json

from app.customer import Customer
from app.shop import Shop


def create_class(
        class_name: object,
        data: list[dict]
) -> list[Customer | Shop]:
    result_list = []
    for item in data:
        new_object = class_name(**item)
        result_list.append(new_object)
    return result_list


def parser(file_name: str) -> tuple[float, list[Customer], list[Shop]]:
    with open(file_name) as json_file:
        config_file = json.load(json_file)
    fuel_price = config_file["FUEL_PRICE"]
    customers = create_class(Customer, config_file["customers"])
    shops = create_class(Shop, config_file["shops"])
    return fuel_price, customers, shops
