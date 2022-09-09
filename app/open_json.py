import json


with open("config.json") as file:
    config_json = json.load(file)

"""
There are 3 users in the customers list now
Call with commands: customers[0], customers[1], customers[2]
"""

customers = []
for i in range(len(config_json["customers"])):
    customers.append(config_json["customers"][i])

"""
There are 3 shops in the shops list now
Call with commands: shops[0], shops[1], shops[2]
"""

shops = []
for i in range(len(config_json["shops"])):
    shops.append(config_json["shops"][i])
