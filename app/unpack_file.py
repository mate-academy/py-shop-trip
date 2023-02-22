import json
from pprint import pprint

with open("app/config.json", "r") as file:
    date = json.load(file)
    fuel_price = date["FUEL_PRICE"]
    customer_list = date["customers"]
    shop_list = date["shops"]


if __name__ == "__main__":
    pprint(customer_list)
