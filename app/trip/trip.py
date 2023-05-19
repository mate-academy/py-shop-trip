from math import dist
from app.shop import Shop
from app.customer import Customer
from app.trip.shop import go_to_shop


def calculate_cost_of_the_trip(
    customer: Customer, fuel_price: float, shop: Shop
) -> float:
    distance = dist(customer.location, shop.location)
    cost_1 = round(
        (customer.car.fuel_consumption / 100)
        * (distance * 2) * fuel_price, 2
    )
    cost_2 = 0
    for product, quantity in customer.wanted_products.items():
        cost_2 += shop.provided_products.get(product, 0) * quantity
    return cost_1 + cost_2


def choose_shop(customer: Customer,
                shops: list[Shop],
                fuel_price: float) -> int:
    result = []
    for shop in shops:
        trip_costs = calculate_cost_of_the_trip(
            customer, fuel_price, shop
        )
        result.append(trip_costs)
        print(f"{customer.name}'s trip to the "
              f"{shop.name} " f"costs {trip_costs}")
    return result.index(min(result))


def can_afford_trip(customer: Customer,
                    shops: list[Shop],
                    fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    cheapest_shop = choose_shop(customer, shops, fuel_price)
    trip_cost = calculate_cost_of_the_trip(
        customer, fuel_price, shops[cheapest_shop]
    )
    if trip_cost < customer.money:
        go_to_shop(customer, shops[cheapest_shop], fuel_price)
    else:
        print(
            f"{customer.name} "
            "doesn't have enough money "
            "to make a purchase in any shop"
        )
