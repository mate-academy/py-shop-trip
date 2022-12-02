import json
from app.customer import Customers
from app.shop import Shop


def price_for_fuel(customer: Customers, shop: Shop) -> float:
    with open("app/config.json") as f:
        file_ = json.load(f)
    fuel_price = file_["FUEL_PRICE"]
    x1 = customer.location[0]
    y1 = customer.location[1]
    x2 = shop.location[0]
    y2 = shop.location[1]
    distance_to_shop = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    fuel_consumption = customer.car["fuel_consumption"]
    spend_liters = (distance_to_shop * fuel_consumption) / 100
    price_for_trip_in_both_way = 2 * spend_liters * fuel_price
    return price_for_trip_in_both_way
