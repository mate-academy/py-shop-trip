import json


from app.shop import Shop
from app.customer import Customer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def shop_trip():
    with open(BASE_DIR / "config.json", "r") as file:
        config_data = json.load(file)
    fuel_price = config_data["FUEL_PRICE"]
    customers_list = [Customer(**cust) for cust in config_data["customers"]]
    shops_list = [Shop(**shop) for shop in config_data["shops"]]
    for customer in customers_list:
        customer.visit_shop(shops_list, fuel_price)
