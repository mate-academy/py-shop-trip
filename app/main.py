import json
import datetime

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    customers = list()
    shops = dict()

    with open("app/config.json", "r") as config:
        db_data = json.load(config)

    f_price = db_data["FUEL_PRICE"]
    for customer in db_data["customers"]:
        customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"],
                customer["car"]["fuel_consumption"])
        ))

    for shop in db_data["shops"]:
        shops[shop["name"]] = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop_distance = dict()
        for shop in shops.values():
            trip_price = customer.trip_price_to(shop.location, f_price) * 2
            trip_price += shop.bill(customer.products_to_buy)[0]
            trip_price = round(trip_price, 2)
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {trip_price}")
            shop_distance[shop.name] = trip_price

        sorted_distances = dict(
            sorted(shop_distance.items(), key=lambda item: item[1])
        )
        best_shop = list(sorted_distances.keys())[0]

        if customer.money < sorted_distances[best_shop]:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {best_shop}")
        print()
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        customer.location = shops[best_shop].location

        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total, bill = shops[best_shop].bill(customer.products_to_buy)
        customer.money = round(customer.money - sorted_distances[best_shop], 2)
        for line in bill:
            print(line)

        print(f"Total cost is {total} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars")
        customer.location = customer.home_location

        print()
