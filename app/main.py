import json
import math

from app.customer import Customer
from app.shop import Shop


def calculate_distance(point1: list, point2: list) -> float:
    return math.sqrt(
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2)


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer.from_dict(c) for c in config["customers"]]
    shops = [Shop.from_dict(s) for s in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        shops_cost = {}

        for shop in shops:
            distance_to_shop = calculate_distance(
                customer.location,
                shop.location)
            distance_back_home = calculate_distance(
                shop.location,
                customer.home_location)
            fuel_cost = ((customer.car.fuel_consumed(distance_to_shop)
                          + customer.car.fuel_consumed(distance_back_home))
                         * fuel_price)
            products_cost = shop.calculate_cart(
                customer.product_cart
            )["total_cost"]
            total_cost = fuel_cost + products_cost

            shops_cost[shop] = total_cost
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost:.2f}")
        cheapest_shop = min(shops_cost, key=shops_cost.get)
        cost = shops_cost[cheapest_shop]

        if customer.money >= cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            print()
            cheapest_shop.make_receipt(customer.name, customer.product_cart)
            customer.relocate(cheapest_shop.location)
            customer.spend_money(cost)
            customer.return_home()
            print()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now "
                  f"has {customer.money:.2f} dollars")
            print()
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
