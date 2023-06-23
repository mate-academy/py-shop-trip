from typing import Union
import math
import json
from app.customer import Customer
from app.shop import Shop


def gas_cost(
        customer_location: list,
        shop_location: list,
        fuel_consumption: Union[int | float]
) -> Union[float | int]:

    with open(
            "app/config.json"
    ) as f:
        config = json.load(f)
        fuel_price = config["FUEL_PRICE"]

    distance = 2 * (math.dist(customer_location, shop_location))
    return round((distance * (fuel_consumption / 100) * fuel_price), 2)


def gas_trip_cost(c_list: list[Customer], s_list: list[Shop]) -> None:
    for customer in c_list:
        for shop in s_list:
            customer.gas_prices[shop.name] += gas_cost(
                customer.location,
                shop.location,
                customer.car["fuel_consumption"]
            )
