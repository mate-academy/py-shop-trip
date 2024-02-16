import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        trip_info = json.load(config)

    fuel_price = trip_info["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in trip_info["customers"]]
    shops = [Shop(**shop) for shop in trip_info["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trips = {}

        for shop in shops:
            distance = shop.get_distance(customer.location, shop.location)
            fuel_cost = customer.car.get_cost_trip(distance, fuel_price)
            products_price = shop.get_product_cost(customer.product_cart)

            trip_price = fuel_cost * 2 + products_price
            trips[shop] = trip_price

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(trip_price, 2)}")

        cheapest_shop = min(trips, key=trips.get)
        shop_location = shop.location
        home_location = customer.location

        if customer.money >= trips[cheapest_shop]:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = shop_location
            customer.make_purchase(cheapest_shop.products)
            print(f"\n{customer.name} rides home")
            customer.location = home_location
            customer.money -= trips[cheapest_shop]
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  "to make a purchase in any shop")
