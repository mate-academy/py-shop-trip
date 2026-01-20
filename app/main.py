import json

from app.customer import Customer
from app.shop import Shop, find_trip_cost, shopping


def shop_trip() -> None:
    with open("app/config.json", "r") as data:
        total_data = json.load(data)

    for customer_data in total_data["customers"]:
        customer = Customer(*customer_data.values())
        print(f"{customer.name} has {customer.money} dollars")

        shops = {}
        for shop_data in total_data["shops"]:
            shop = Shop(*shop_data.values())
            trip_cost = find_trip_cost(
                customer.location,
                shop.location,
                total_data["FUEL_PRICE"],
                customer.car["fuel_consumption"]
            )
            total_costs = (
                trip_cost
                + sum(value * shop.products[key]
                      for key, value in customer.product_cart.items())
            )
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {total_costs}"
            )
            shops[total_costs] = shop

        the_nearest_shop = shops[min(shops)]
        if customer.money < min(shops):
            return print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
        print(f"{customer.name} rides to {the_nearest_shop.name}\n")

        shopping(
            customer.name,
            customer.product_cart,
            the_nearest_shop.products
        )

        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now has {customer.money - min(shops)} dollars\n"
        )
