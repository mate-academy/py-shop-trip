import json


with open("app/config.json", "r") as file_json:
    fuel_price = json.load(file_json)["FUEL_PRICE"]
