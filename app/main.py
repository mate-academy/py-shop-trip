import json
from decimal import Decimal
from math import inf

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        data = json.load(config_file)

    fuel_price = Decimal(str(data["FUEL_PRICE"]))

    shops = [Shop.from_dict(shop_dict) for shop_dict in data["shops"]]

    customers = [
        Customer.from_dict(customer_dict)
        for customer_dict in data["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        picked_shop = None
        picked_route_cost = Decimal(float(inf))
        for shop in shops:
            ride_cost = customer.calculate_ride_cost_to(
                shop.location, fuel_price
            )
            products_cost = sum(
                shop.calculate_prices_for_products(customer.product_cart)
            )
            trip_cost = Decimal(round(ride_cost * 2 + products_cost, 2))
            print(
                f"{customer.name}'s trip to the "
                + f"{shop.name} costs "
                + f"{trip_cost}"
            )

            if trip_cost < picked_route_cost:
                picked_shop = shop
                picked_route_cost = trip_cost

        if picked_route_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                + "to make a purchase in any shop"
            )
            return

        home_location = customer.location
        print(f"{customer.name} rides to {picked_shop.name}")
        customer.go_to(picked_shop.location)

        print(picked_shop.get_receipt(customer))

        print(f"{customer.name} rides home")
        customer.go_to(home_location)

        customer.count_remaining_money(picked_route_cost)
        print(f"{customer.name} now has {customer.money} dollars\n")
