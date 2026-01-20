from app.customer import Customer
from app.shop import Shop
from app.data_initial import data


def calculate_distance(location1: list, location2: list) -> float:
    x1, y1 = location1
    x2, y2 = location2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * 2
    return round(distance, 2)


def calculate_trip_cost(
        distance: float,
        fuel_consumption: float,
        fuel_price: float = data["FUEL_PRICE"]
) -> float:
    fuel_needed = (fuel_consumption / 100) * distance
    trip_cost = fuel_needed * fuel_price
    return round(trip_cost, 2)


def calculate_purchase_price(
        trip_cost: float,
        customer: Customer,
        shop: Shop
) -> float:
    result = trip_cost
    for buy_key, value in customer.products.items():
        for sell_key, cost in shop.product_cost.items():
            if buy_key == sell_key:
                result += value * cost
    return round(result, 2)
