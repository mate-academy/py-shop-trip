import Classes
from Classes import CUSTOMER_LIST, SHOP_LIST, FUEL_PRICE


def shop_trip() -> None:
    Classes.get_data("config.json")
    for customer in CUSTOMER_LIST:
        cheapest_shop, cost = customer.calculate_trip_cost(SHOP_LIST,
                                                           FUEL_PRICE)
        customer.trip_to_cheapest(cheapest_shop, cost)


shop_trip()
