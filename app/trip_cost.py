import math
from decimal import Decimal, ROUND_HALF_UP
from typing import List
from app.customer import Customer
from app.shop import Shop
from app.config import data_config
from app.in_the_shop import shopping_in_the_store
from app.products_cost import calculate_products_cost
from app.ride_home import ride_home


def calculate_trip_cost(list_of_customers: List[Customer],
                        list_of_shops: List[Shop]) -> None:
    fuel_price = Decimal(str(data_config["FUEL_PRICE"]))
    cheapest_trip = dict()
    for customer in list_of_customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in list_of_shops:
            distance_to_shop = Decimal(str((
                math.sqrt((shop.location[0] - customer.location[0])
                          ** 2 + (shop.location[1] - customer.location[1])
                          ** 2))))
            road_trip_consumption =\
                Decimal(str(2 * ((customer.car.fuel_consumption
                                  * distance_to_shop) / 100)))
            road_trip_cost = fuel_price * road_trip_consumption
            product_cart_cost = calculate_products_cost(customer, shop)
            trip_cost = road_trip_cost + product_cart_cost
            total_cost = trip_cost.quantize(Decimal("0.00"),
                                            rounding=ROUND_HALF_UP)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {total_cost}")
            cheapest_trip[shop] = total_cost

        min_cost_per_customer = min(cheapest_trip.items(), key=lambda x: x[1])
        if customer.money >= min_cost_per_customer[1]:
            print(f"{customer.name} rides to {min_cost_per_customer[0].name}\n"
                  f"")
            customer.location = min_cost_per_customer[0].location
            shopping_in_the_store(customer, min_cost_per_customer[0])
            ride_home(customer, min_cost_per_customer[1])
        else:
            print(f"{customer.name} doesn't have"
                  f" enough money to make a purchase in any shop")
    return
