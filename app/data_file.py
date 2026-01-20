import json


with open("app/config.json", "r") as config:
    data_file = json.load(config)


fuel_price = float(data_file["FUEL_PRICE"])
customers = data_file["customers"]
shops = data_file["shops"]
