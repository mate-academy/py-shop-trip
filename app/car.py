from typing import Union
import math
from app.customer import Customer
from app.shop import Shop


def gas_cost(
        customer_location: list,
        shop_location: list,
        fuel_consumption: Union[int | float],
        config_file: dict
) -> Union[float | int]:

    fuel_price = config_file["FUEL_PRICE"]

    distance = 2 * (math.dist(customer_location, shop_location))
    return round((distance * (fuel_consumption / 100) * fuel_price), 2)


def gas_trip_cost(
        customers: list[Customer],
        shops: list[Shop],
        config_file: dict
) -> None:
    for customer in customers:
        for shop in shops:
            customer.gas_prices[shop.name] += gas_cost(
                customer.location,
                shop.location,
                customer.car["fuel_consumption"],
                config_file
            )
