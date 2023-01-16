import json
from app.classes import Customer, Shop, Car


def unload() -> dict:
    with open("app/config.json", "r") as data:
        output = json.load(data)
    return output


def create_customers(json_input: dict) -> list[Customer]:
    customers_list = []
    for customer in json_input["customers"]:
        customers_list.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            )
        )
    return customers_list


def create_shops(json_input: dict) -> list[Shop]:
    shops_list = []
    for shop in json_input["shops"]:
        shops_list.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )
    return shops_list


JSON_OUTPUT = unload()
FUEL_PRICE = JSON_OUTPUT["FUEL_PRICE"]
CUSTOMERS = create_customers(JSON_OUTPUT)
SHOPS = create_shops(JSON_OUTPUT)
