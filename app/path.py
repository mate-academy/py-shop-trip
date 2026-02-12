import json
import os

path = os.path.join("app", "config.json")
with open(path, "r") as config_data:
    config_data = json.load(config_data)
fuel_price = config_data.get("FUEL_PRICE")
shops = config_data.get("shops")
customers = config_data.get("customers")
