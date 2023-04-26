import json

from app.classes import Customer, Shop

with open("app/config.json") as file:
    data = json.load(file)

fuel_price = data["FUEL_PRICE"]
customers_list = data["customers"]
shops_list = data["shops"]

customers = [Customer(*customer.values()) for customer in customers_list]
shops = [Shop(*shop.values()) for shop in shops_list]
