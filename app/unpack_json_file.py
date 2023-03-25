import json

with open("app/config.json", "r") as file:
    data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    list_of_customers = data["customers"]
    list_of_shops = data["shops"]
