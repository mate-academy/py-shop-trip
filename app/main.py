import json
import app.functions
import os


def shop_trip() -> None:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "config.json")

    with open(file_path, "r") as config:
        data = json.load(config)
        customers_json = data.get("customers")
        shops_json = data.get("shops")

    fuel_price = data.get("FUEL_PRICE")

    customers = app.functions.create_list_of_customers_objects(
        customers_json
    )
    shops = app.functions.create_list_of_shops_objects(shops_json)

    for customer in customers:
        correct_shop = customer.find_the_cheapest_shop(shops, fuel_price)
        if correct_shop:
            customer.ride_purchase_ask_the_receipt(correct_shop)
