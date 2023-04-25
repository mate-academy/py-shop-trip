import json

with open("config.json") as file:
    data = json.load(file)


def from_json(custom_class, instances):
    instance = custom_class()

