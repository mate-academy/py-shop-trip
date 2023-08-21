import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop, make_shop_trip
from app.error import InitialDataError
from os import path


def shop_trip() -> None:

    file_name = path.join("app", "config.json")
    with open(file_name, "r") as config:

        trips_data = json.load(config)

        if not trips_data.get("FUEL_PRICE"):
            raise InitialDataError("FUEL_PRICE not set in file")

        shop_list = [
            Shop(store["name"], store["location"], store["products"])
            for store in trips_data.get("shops")
        ]

        customer_list = [
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"].get("brand", ""),
                    customer["car"]["fuel_consumption"]
                )
            )
            for customer in trips_data.get("customers")
        ]

        for customer in customer_list:
            make_shop_trip(customer, shop_list, trips_data["FUEL_PRICE"])
