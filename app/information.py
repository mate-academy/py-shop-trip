import json


def customers_information():
    with open("C:\\Users\\vpano\\py-shop-trip\\app\\config.json") as file:
        information = json.load(file)
        return information
