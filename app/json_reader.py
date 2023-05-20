import json
import os

path_file = os.path.abspath(".")
path_file = os.path.join(path_file, "app", "config.json")
with open(path_file, "r") as cars_file:
    data = json.load(cars_file)
    fuel_price = data["FUEL_PRICE"]
