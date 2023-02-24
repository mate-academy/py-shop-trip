import json
from app.visit_shop import visit_shop, get_customers, get_shops


def shop_trip() -> None:
    with open("app/config.json") as open_file:
        data = json.load(open_file)

    customers_list = get_customers(data["customers"])
    fuel_price = data["FUEL_PRICE"]

    shops_list = get_shops(data["shops"])

    for customer in customers_list:
        visit_shop(customer, shops_list, fuel_price)
