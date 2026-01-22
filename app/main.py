import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        data = json.load(config_file)
        customers = data["customers"]
        shops = data["shops"]

    for person in customers:
        customer = Customer(
            person["name"],
            person["product_cart"],
            person["location"],
            person["money"],
        )
        car = Car(person["car"]["brand"], person["car"]["fuel_consumption"])
        print(customer)

        prices = {}
        for shop in shops:
            shop_inst = Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            fuel_cost = (data["FUEL_PRICE"]
                         * car.litres_per_trip(shop_inst, customer))
            total = round(fuel_cost * 2 + shop_inst.shopping_cost(customer), 2)
            prices[total] = shop_inst
            print(f"{customer.name}'s trip to the {shop_inst.name} "
                  f"costs {total}")

        if customer.money >= min(prices):
            cheapest_shop = prices[min(prices)]
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            customer.money -= min(prices)
            cheapest_shop.issue_receipt(customer)
            print(
                f"\n{customer.name} rides home"
                f"\n{customer.name} now has {customer.money} dollars\n"
            )
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
