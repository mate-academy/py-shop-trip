import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_info = json.load(file)
        customers = json_info["customers"]
        shops = json_info["shops"]

    customer_list = list()
    shop_list = list()

    for customer in customers:
        customer_list.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"])
            )
        )

    for current_shop in shops:
        shop_list.append(
            Shop(
                current_shop["name"],
                current_shop["location"],
                current_shop["products"]
            )
        )

    for person in customer_list:
        print(f"{person.name} has {person.money} dollars")

        costs_of_trips = dict()
        for shop in shop_list:
            cost_of_products = shop.cost_of_all_products(person.product_cart)
            cost_of_the_trip = person.cost_of_the_trip(shop) + cost_of_products
            print(f"{person.name}'s trip to the "
                  f"{shop.name} costs {cost_of_the_trip}")
            costs_of_trips[shop] = cost_of_the_trip

        shop_to_go = min(costs_of_trips, key=costs_of_trips.get)

        if costs_of_trips[shop_to_go] > person.money:
            print(f"{person.name} doesn't have enough money"
                  f" to make purchase in any shop")
            return
        shop_to_go.shopping(person)
        print(f"{person.name} rides home\n"
              f"{person.name} now has "
              f"{person.money - costs_of_trips[shop_to_go]} dollars\n")
