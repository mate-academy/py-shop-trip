import json
from app.classes.customer import Customer
from app.classes.shop import Shop

CONST = "app/config.json"

with open(CONST, "r") as file:
    data = json.load(file)


fuel_price = data["FUEL_PRICE"]
customers_data = data["customers"]
shops_data = data["shops"]

shops = [Shop(**shop) for shop in shops_data]
customers = [Customer(**customer) for customer in customers_data]
