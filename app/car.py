from typing import Union
import math
import json
from app.customer import Customer
from app.shop import Shop


def gas_cost(
        c_location: list,
        s_location: list,
        fuel_consumption: Union[int | float]
) -> Union[float | int]:

    with open(
            "/Users/anton/Projects/py-shop-trip/app/config.json"
    ) as f:
        config = json.load(f)
        fuel_price = config["FUEL_PRICE"]

    distance = 2 * (math.dist(c_location, s_location))
    return round((distance * (fuel_consumption / 100) * fuel_price), 2)


def gas_trip_cost(c_list: list[Customer], s_list: list[Shop]) -> None:
    for customer in c_list:
        for shop in s_list:
            if shop.name == "Outskirts Shop":
                customer.gas_prices["Outskirts Shop"] += gas_cost(
                    customer.location,
                    shop.location,
                    customer.car["fuel_consumption"]
                )
            if shop.name == "Shop '24/7'":
                customer.gas_prices["Shop '24/7'"] += gas_cost(
                    customer.location,
                    shop.location,
                    customer.car["fuel_consumption"]
                )
            if shop.name == "Central Shop":
                customer.gas_prices["Central Shop"] += gas_cost(
                    customer.location,
                    shop.location,
                    customer.car["fuel_consumption"]
                )
