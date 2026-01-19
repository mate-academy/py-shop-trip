from app.customer import Customer
from app.shop import Shop


def calc_distance_cost(
        customer: Customer,
        shop: Shop,
        fuel_prise: int | float
) -> float | int:
    distance_cost = customer.car.fuel_needed_for_trip(
        customer.calculate_distance(shop.location)
    ) * fuel_prise

    return distance_cost


def calc_purchases_cost(
        customer: Customer,
        shop: Shop
) -> float | int:
    return customer.purchases_cost(shop.products)
