import json
from math import dist

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_info = json.load(file)
    fuel_price = json_info["FUEL_PRICE"]
    customers = json_info["customers"]
    shops = json_info["shops"]

    customer_list = []
    shop_list = []

    for customer in customers:
        new_customer = Customer(customer["name"],
                                customer["product_cart"],
                                customer["location"],
                                customer["money"],
                                Car(
                                    customer["car"]["brand"],
                                    customer["car"]["fuel_consumption"])
                                )
        customer_list.append(new_customer)

    for current_shop in shops:
        new_shop = Shop(
            current_shop["name"],
            current_shop["location"],
            current_shop["products"]
        )
        shop_list.append(new_shop)

    for person in customer_list:
        print(f"{person.name} has {person.money} dollars")
        costs_of_trips = {}

        for shop in shop_list:
            distance_to_the_shop = dist(person.location, shop.location)
            product_cost = shop.cost_of_all_products(person.product_cart)
            trip_cost = round((person.car.fuel_consumption / 100)
                              * (distance_to_the_shop * 2)
                              * fuel_price, 2) + product_cost
            print(f"{person.name}'s trip to the {shop.name} costs {trip_cost}")
            costs_of_trips[shop] = trip_cost

        cheapest_trip = min(costs_of_trips, key=costs_of_trips.get)

        if costs_of_trips[cheapest_trip] > person.money:
            print(f"{person.name} doesn't have enough money"
                  f" to make purchase in any shop")
            return
        print(f"{person.name} rides to {cheapest_trip.name}\n")
        person.location = cheapest_trip.location
        print("Date: 04/01/2021 12:33:41\n"
              f"Thanks, {person.name}, for you purchase!\n"
              "You have bought: ")
        total_cost = 0

        for item, amount in person.product_cart.items():
            cost_of_product = amount * cheapest_trip.products[item]
            print(f"{amount} {item}s for {cost_of_product} dollars")
            total_cost += cost_of_product

        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n"
              f"\n"
              f"{person.name} rides home\n"
              f"{person.name} now has "
              f"{person.money - costs_of_trips[cheapest_trip]} dollars\n")
