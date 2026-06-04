from app import shop
from app import car
from app import customer
import json


def shop_trip() -> None:

    with open("./app/config.json", "r") as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]

    shops = [shop.Shop(**shop_data) for shop_data in data["shops"]]

    customers = [
        customer.Customer(
            name=cust_data["name"],
            product_cart=cust_data["product_cart"],
            location=cust_data["location"],
            money=cust_data["money"],
            car=car.Car(**cust_data["car"])
        )
        for cust_data in data["customers"]
    ]

    for person in customers:
        print(f"{person.name} has {person.money} dollars")

        best_shop = None
        cheapest_cost = float("inf")

        for current_shop in shops:
            trip_cost = person.get_trip_cost(current_shop, fuel_price)
            print(f"{person.name}'s trip to the {current_shop.name} "
                  f"costs {round(trip_cost, 2)}")

            if trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                best_shop = current_shop

        if person.money >= cheapest_cost:
            person.go_to_shop(best_shop, fuel_price)
        else:
            print(f"{person.name} doesn't have enough money "
                  f"to make a purchase in any shop")

        if person != customers[-1]:
            print()
