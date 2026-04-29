import json

from app.shop import Shop
from app.customer import Customer


with open("app/config.json", "r") as config_file:
    config = json.load(config_file)

fuel_price, customers, shops = config.values()
customers_objects = [Customer(**customer) for customer in customers]
shops_objects = [Shop(**shop) for shop in shops]


def shop_trip() -> None:
    for customer in customers_objects:
        print(f"{customer.name} has {customer.money} dollars")
        trips_costs = {}
        for shop in shops_objects:
            cost_shop_trip = customer.price_for_shop_trip(shop, fuel_price)
            trips_costs[cost_shop_trip] = shop.name
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {cost_shop_trip}"
            )

        if customer.money >= min(trips_costs):
            chosen_shop_name = trips_costs[min(trips_costs)]
            home_location = customer.location
            print(f"{customer.name} rides to {chosen_shop_name}\n")
            chosen_shop = list(
                filter(
                    lambda shop_: shop_.name == chosen_shop_name, shops_objects
                )
            )[0]
            customer.location = chosen_shop.location
            customer.receipt(chosen_shop)
            print(f"{customer.name} rides home")
            customer.location = home_location
            customer.money -= min(trips_costs)
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(
                f"{customer.name} "
                f"doesn't have enough money to make a purchase in any shop"
            )
