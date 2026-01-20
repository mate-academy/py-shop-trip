import json

from app.customer import load_customers_from_json
from app.shop import load_shops_from_json


def shop_trip() -> None:
    configuration_file = "app/config.json"

    customers = load_customers_from_json(configuration_file)
    shops = load_shops_from_json(configuration_file)
    with open(configuration_file, "r") as json_file:
        fuel_price = json.load(json_file)["FUEL_PRICE"]

    for customer in customers:
        customer.print_balance()
        shop_to_visit = customer.choose_shop_to_visit(shops, fuel_price)

        if shop_to_visit is not None:
            customer.buy_products(shop_to_visit)
            customer.go_home()
