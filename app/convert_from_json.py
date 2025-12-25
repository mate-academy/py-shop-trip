import json

with open("app/config.json", "r") as file:
    trip_info = json.load(file)
    shop_list = trip_info["shops"]
    customers = trip_info["customers"]
    FUEL_PRICE = trip_info["FUEL_PRICE"]
