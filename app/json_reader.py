import json

from app.customer import Customer
from app.info_dict import InfoDict
from app.shop import Shop


def read_json() -> InfoDict:
    with open("app/config.json", "r") as file_open:
        data = json.load(file_open)

    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]

    return InfoDict(
        customers=customers,
        shops=shops,
        fuel_price=fuel_price
    )
