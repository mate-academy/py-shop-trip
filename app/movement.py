import json
from os import remove


def trip_to_the_store(customer, shop):
    location_home = customer["location"]
    with open("location_home.json", "w") as file:
        json.dump(location_home, file)
    customer["location"][0] = shop["location"][0]
    customer["location"][1] = shop["location"][1]


def trip_to_the_home(customer):
    with open("location_home.json") as file:
        location_home = json.load(file)
    customer["location"][0] = location_home[0]
    customer["location"][1] = location_home[1]
    remove("location_home.json")
