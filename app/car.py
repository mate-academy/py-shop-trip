import json


with open("app/config.json", "r") as file:
    fuel_price = json.load(file)["FUEL_PRICE"]
