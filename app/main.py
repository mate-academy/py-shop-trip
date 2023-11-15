import json
import datetime

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]

    for customer in customers:
        customer = Customer(**customer)
        name = customer.name
        print(f"{customer.name} has {customer.money} dollars")
        min_trip_cost = None

        for shop in shops:
            shop = Shop(**shop)
            cost_to_shop = customer.cost_to_shop(shop) * fuel_price
            product_cost = customer.product_cost(shop)
            trip_cost = round(cost_to_shop * 2 + product_cost, 2)
            print(f"{name}'s trip to the {shop.name} costs {trip_cost}")

            if min_trip_cost is None or trip_cost < min_trip_cost[1]:
                min_trip_cost = [shop, trip_cost, product_cost]

        shop = min_trip_cost[0]
        product_cost = min_trip_cost[2]
        min_trip_cost = min_trip_cost[1]

        if min_trip_cost > customer.money:
            print(f"{name} doesn't have enough money"
                  f" to make a purchase in any shop")
            continue
        print(f"{name} rides to {shop.name}\n")
        print(f"Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")

        customer.print_product_list(shop)
        print(f"Total cost is {product_cost} dollars")
        print("See you again!\n")

        print(f"{name} rides home")
        customer.money -= min_trip_cost
        print(f"{name} now has {customer.money} dollars\n")
