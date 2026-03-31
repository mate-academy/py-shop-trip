import json


with open("app/config.json") as file:
    data = json.load(file)

try:
    fuel_price = data["FUEL_PRICE"]
except KeyError:
    raise Exception("Fuel price is missing")
