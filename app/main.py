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

        shop_list = []
        for store in trips_data.get("shops"):
            if (store.get("name")
                    and store.get("location")
                    and store.get("products")):
                current_shop = Shop(
                    store["name"],
                    store["location"],
                    store["products"]
                )
                shop_list.append(current_shop)

        customer_list = []
        for customer in trips_data.get("customers"):
            if (customer.get("car")
                    and customer["car"].get("fuel_consumption")
                    and customer.get("name")
                    and customer.get("product_cart")
                    and customer.get("location")
                    and customer.get("money")):
                current_car = Car(
                    customer["car"].get("brand", ""),
                    customer["car"]["fuel_consumption"]
                )
                current_customer = Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    current_car
                )
                customer_list.append(current_customer)

        for customer in customer_list:
            make_shop_trip(customer, shop_list, trips_data["FUEL_PRICE"])
