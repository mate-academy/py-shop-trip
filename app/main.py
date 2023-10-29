import json
from datetime import datetime

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        shopping_data = json.load(file)

    fuel_cost = shopping_data["FUEL_PRICE"]
    customer_list = []
    shop_list = []

    for customer in shopping_data["customers"]:
        person = Customer(customer["name"],
                          customer["product_cart"],
                          customer["location"],
                          customer["money"],
                          Car(customer["car"]["brand"],
                              customer["car"]["fuel_consumption"],
                              fuel_cost)
                          )
        customer_list.append(person)

    for shop in shopping_data["shops"]:
        store = Shop(shop["name"],
                     shop["location"],
                     shop["products"]
                     )
        shop_list.append(store)

    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs_list = {}
        shop_receipts_list = {}

        for shop in shop_list:
            shop_info = customer.handle_order(shop)
            product_total_cost = shop_info.get("total_prod_cost")
            trip_cost = customer.calculate_trip_cost(shop,
                                                     customer.car,
                                                     fuel_cost)
            total_cost = product_total_cost + trip_cost
            trip_costs_list[shop.name] = total_cost
            shop_receipts_list[shop.name] = shop_info
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost}")

        min_cost_trip_shop = sorted(trip_costs_list.items(),
                                    key=lambda x: x[1])[0]

        if customer.money >= min_cost_trip_shop[1]:
            min_receipt_shop = shop_receipts_list.get(min_cost_trip_shop[0])
            customer.location = min_receipt_shop["shop_location"]
            time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"{customer.name} rides to {min_cost_trip_shop[0]}")
            print()
            print(f"Date: {time_stamp}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for item, value in min_receipt_shop.items():
                if item != "total_prod_cost" and item != "shop_location":
                    print(f"{customer.product_list[item]} "
                          f"{item}s for {value} dollars")

            print(f"Total cost is {min_receipt_shop['total_prod_cost']} "
                  f"dollars")
            print("See you again!")
            print()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min_cost_trip_shop[1]} dollars")
            print()
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
