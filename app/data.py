import json


with open("app/config.json", "r") as f:
    data = json.load(f)

customers_list = [customer for customer in data["customers"]]
shops_list = [shop for shop in data["shops"]]
fuel_price = data["FUEL_PRICE"]
