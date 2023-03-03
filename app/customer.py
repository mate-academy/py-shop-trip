import json
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")
location_customer = {}
fuel_consumption_car = {}


def customers_and_content() -> list:
    with open(relative_path, "r") as file:
        global content
        content = json.load(file)
    global customers
    customers = content.get("customers")
    return customers, content
