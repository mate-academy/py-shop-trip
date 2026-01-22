import json

from app.customer import create_customer_from_dict
from app.shop import create_shop_from_dict


def shop_trip() -> None:

    with open("app/config.json", "r") as json_file:
        config = json.load(json_file)

    customers = [
        create_customer_from_dict(person) for person in config["customers"]
    ]
    shops = [create_shop_from_dict(shop) for shop in config["shops"]]
    fuel_price = config["FUEL_PRICE"]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs_to_different_shops = {}

        for shop in shops:
            distance = customer.location.distance_to_location(shop.location)
            fuel_cost = ((customer.car.fuel_consumption * fuel_price / 100)
                         * distance)
            products_cost = shop.buy_products_from_cart(customer.product_cart)
            trip_cost = round(fuel_cost * 2 + products_cost, 2)
            trip_costs_to_different_shops[shop] = trip_cost
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")
        cheapest_shop = min(
            trip_costs_to_different_shops,
            key=trip_costs_to_different_shops.get
        )
        need_money = trip_costs_to_different_shops[cheapest_shop]

        if customer.money >= need_money:
            home = customer.location
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location
            print(cheapest_shop.print_check(customer))
            customer.location = home
            print(f"{customer.name} rides home")
            customer.money -= need_money
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            break
