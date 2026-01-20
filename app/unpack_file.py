import json


def open_file() -> dict:
    with open("app/config.json", "r") as file:
        date = json.load(file)
        fuel_price = date["FUEL_PRICE"]
        customer_list = date["customers"]
        shop_list = date["shops"]
    return {
        "fuel_price": fuel_price,
        "customer_list": customer_list,
        "shop_list": shop_list
    }
