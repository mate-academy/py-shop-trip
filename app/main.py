import json
import os

from app.factories import get_customers, get_shops
import app.point as point


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        trip_data = json.load(file)

    fuel_price = trip_data["FUEL_PRICE"]
    customers = get_customers(trip_data["customers"])
    shops = get_shops(trip_data["shops"])

    for customer in customers:

        total_cost = float("inf")
        cheapest_shop = None
        shopping_cost = None

        customer.print_amount_of_money()

        for shop in shops:
            current_shopping_cost = shop.calculate_shopping(customer)
            distance = point.Point.calculate_distance(
                customer.location,
                shop.location
            )
            current_ride_cost = customer.car.calculate_ride_cost(
                distance,
                fuel_price
            )
            current_total_cost = (
                current_shopping_cost["shopping_cost"]
                + current_ride_cost * 2
            )
            customer.print_trip_cost(shop, current_total_cost)

            if current_total_cost < total_cost:
                total_cost = current_total_cost
                cheapest_shop = shop
                shopping_cost = current_shopping_cost

        if customer.money < total_cost:
            customer.print_not_enough_money()
            continue

        customer.print_ride(cheapest_shop)
        customer.location = cheapest_shop.location
        customer.print_date()
        customer.money = customer.money - total_cost
        customer.print_purchase_info(
            shopping_cost["cart"],
            shopping_cost["shopping_cost"]
        )
        customer.print_ride_home()
        customer.print_amount_of_money(after_shopping=True)
