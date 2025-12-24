import json
from typing import Any, Callable

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> bool or None:

    def error_handler(error_type: type, err_message: str) -> Callable:
        def wrapper(func: Callable) -> Callable:
            def inner(*args, **kwargs) -> Any:
                try:
                    return func(*args, **kwargs)
                except error_type:
                    print(err_message)
                    return False
            return inner
        return wrapper

    err_messages = {
        "json": "The specified file could not be opened or found.",
        "object": "Failed to create class instance. "
                  "Кey not found or invalid value format."
    }

    @error_handler(IOError, err_messages["json"])
    def get_json_data(json_file: str) -> dict or bool:
        with open(json_file, "r") as file:
            cfg = json.load(file)
        return cfg

    @error_handler(KeyError or ValueError, err_messages["object"])
    def create_customers(customers_list: list, cfg: dict) -> bool:
        for customer in cfg:
            car = customer["car"]
            customers_list.append(
                Customer(
                    name=customer["name"],
                    location=customer["location"],
                    money=customer["money"],
                    product_cart=customer["product_cart"],
                    car=Car(
                        brand=car["brand"],
                        fuel_consumption=car["fuel_consumption"]
                    )
                )
            )
        return True

    @error_handler(KeyError or ValueError, err_messages["object"])
    def create_shops(shops_list: list, cfg: dict) -> bool:
        for shop in cfg:
            shops_list.append(
                Shop(
                    name=shop["name"],
                    location=shop["location"],
                    products=shop["products"]
                )
            )
        return True

    customers = []
    shops = []
    fuel_price = selected_costs = selected_shop = None

    config = get_json_data("config.json")

    if config:
        customers_is_set = create_customers(customers, config["customers"])
        shops_is_set = create_shops(shops, config["shops"])
        fuel_price = config["FUEL_PRICE"]

        if customers_is_set and shops_is_set and fuel_price:
            for customer in customers:
                customer.has_dollars()

                for shop in shops:
                    costs_trip = customer.calculate_shop_trip(shop, fuel_price)
                    if selected_shop:
                        if selected_costs > costs_trip:
                            selected_costs = costs_trip
                            selected_shop = shop
                    else:
                        selected_shop = shop
                        selected_costs = costs_trip

                customer.selected_shop = selected_shop
                customer.acquisition_costs = selected_costs

                if customer.visit_the_shop():
                    selected_shop.serve_the_customer(customer)
                    customer.rides_home()
            return True

    return print("Sorry, something went wrong. "
                 "The grocery trip could not be calculated.")
