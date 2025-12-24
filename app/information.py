import json


def customers_information():
    with open("app/config.json") as file:
        information = json.load(file)
        return information
