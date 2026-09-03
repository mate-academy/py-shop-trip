import json

from app.customer import Customer
from app.shop import Shop


def unpack_json(file_name: str) -> list:
    with open(file_name) as json_file:
        info = json.load(json_file)
        fuel_price = info["FUEL_PRICE"]
        customers = [
            Customer.create_customers_from_dict(customer)
            for customer in info["customers"]
        ]
        shops = [Shop.create_shop_from_dict(shop) for shop in info["shops"]]
    return [fuel_price, customers, shops]
