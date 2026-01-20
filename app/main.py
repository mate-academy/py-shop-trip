import json
from customer import Customer
from shop import Shop


def shop_trip() -> None:
    with open("app\\config.json") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"\n{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )

        cheapest_shop = min(
            shops,
            key=lambda shop: customer.calculate_trip_cost(shop, fuel_price)
        )
        if customer.can_afford_trip(cheapest_shop, fuel_price):
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.make_trip(cheapest_shop, fuel_price)
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
