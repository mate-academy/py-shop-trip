import decimal
from decimal import Decimal


def trip_cost(
        customer_location: list,
        shop_location: list,
        fuel_cost: float,
        fuel_consumption: float
) -> decimal.Decimal:

    destination = Decimal(
        ((customer_location[0] - shop_location[0]) ** 2
         + (customer_location[1] - shop_location[1]) ** 2) ** 0.5
    )

    return Decimal(fuel_cost) * Decimal(fuel_consumption) * destination / 100
