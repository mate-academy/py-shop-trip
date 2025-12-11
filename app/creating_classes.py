import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def open_config_file(json_file: json, attribute: str) -> json:
    with open(json_file, attribute) as config_file:
        config = json.load(config_file)
        return config


def creation_class_customer() -> list[Customer]:

    config = open_config_file("app/config.json", "r")

    customers_list = []
    customers = config.get("customers")
    for param in customers:
        customer = Customer(
            param.get("name"),
            param.get("product_cart"),
            param.get("location"),
            param.get("money"),
            car=Car(
                param.get("car").get("brand"),
                param.get("car").get("fuel_consumption"),
                config.get("FUEL_PRICE")
            )
        )
        customers_list.append(customer)

    return customers_list


def creation_class_shop() -> list[Shop]:

    config = open_config_file("app/config.json", "r")

    shops_list = []
    shops = config.get("shops")
    for param in shops:
        shop = Shop(
            param.get("name"),
            param.get("location"),
            param.get("products")
        )
        shops_list.append(shop)

    return shops_list
