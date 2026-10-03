import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        )
        for shop in config["shops"]
    ]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"],
        )
        for customer in config["customers"]
    ]

    for index, customer in enumerate(customers):
        print(
            f"{customer.name} has "
            f"{customer.money:g} dollars"
        )

        trip_costs = []

        for shop in shops:
            cost = customer.get_trip_cost(
                shop,
                fuel_price,
            )
            trip_costs.append((cost, shop))

            print(
                f"{customer.name}'s trip to "
                f"the {shop.name} costs {cost:.2f}"
            )

        cheapest_cost, cheapest_shop = min(
            trip_costs,
            key=lambda trip: trip[0],
        )

        if customer.money >= cheapest_cost:
            customer.make_purchase(
                cheapest_shop,
                cheapest_cost,
            )
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )

        if index < len(customers) - 1:
            print()
