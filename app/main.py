import json

from app.customer import Customer
from app.shop import Shop
from app.utils import shopping_choice, back_home


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        configuration = json.load(config_file)

    fuel_price = configuration["FUEL_PRICE"]
    customers = [Customer(customer) for customer in configuration["customers"]]
    shops = [Shop(shop) for shop in configuration["shops"]]

    for customer in customers:
        if shopping_choice(customer, shops, fuel_price):
            back_home(customer)
