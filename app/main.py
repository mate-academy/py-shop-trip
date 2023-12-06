from app.customer import Customer
from app.shop import Shop

import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        cust_info = data["customers"]
        shop_info = data["shops"]

    customers = [
        Customer(
            info["name"],
            info["location"],
            info["money"],
            info["car"],
            info["product_cart"],
        )
        for info in cust_info
    ]

    shops = [
        Shop(shop_obj["name"], shop_obj["location"], shop_obj["products"])
        for shop_obj in shop_info
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shops_price = {}
        for shop in shops:
            all_prod_cost = shop.calculate_products_cost(customer)
            dist = customer.distance(shop)
            fuel_consumption_price = customer.calculate_fuel_price(
                dist,
                fuel_price
            )
            total_trip_cost = round(
                (all_prod_cost + fuel_consumption_price),
                2
            )
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_trip_cost}")
            shops_price[shop] = total_trip_cost
        cheapest_shop = min(shops_price, key=shops_price.get)
        cheapest_price = shops_price[cheapest_shop]

        if customer.money >= cheapest_price:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.receipt(customer)
            print(f"{customer.name} rides home")
            remaining_money = customer.money - cheapest_price
            print(f"{customer.name} now has {remaining_money} dollars\n")

        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
