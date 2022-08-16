import json


with open("app/config.json", "r") as f:
    data = json.load(f)

cust_list = [customer for customer in data["customers"]]
shop_list = [shop for shop in data["shops"]]
fuel_price = data["FUEL_PRICE"]
