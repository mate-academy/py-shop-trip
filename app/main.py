import json
import datetime
from app.car import Car
from app.customer import Customer
from app.shop import Shop
import os


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.json")
    with open(config_path) as file:
        data = json.load(file)

    fuel = data["FUEL_PRICE"]
    list_customers = []
    for number in range(len(data["customers"])):
        customer_data = (data["customers"][number])
        list_customers.append(Customer(customer_data["name"],
                                       customer_data["product_cart"],
                                       customer_data["location"],
                                       customer_data["money"],
                                       Car(customer_data["car"]["brand"],
                                           customer_data["car"]
                                           ["fuel_consumption"])))
    list_shops = []
    for number in range(len(data["shops"])):
        dictionary = (data["shops"][number])
        list_shops.append(Shop(dictionary["name"],
                               dictionary["location"],
                               dictionary["products"]))
    for customer in list_customers:
        customer.printer(list_shops, fuel)
        cheapest_shop = customer.cheapest(list_shops, fuel)
        if customer.money < customer.trip_cost(cheapest_shop, fuel):
            print(f"{customer.name}"
                  f" doesn't have enough money to"
                  f" make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {cheapest_shop.name}")
        original_location = customer.location
        customer.location = cheapest_shop.location
        print("")
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {current_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        customer.buy_at_shop(cheapest_shop)
        print("")
        print(f"{customer.name} rides home")
        customer.location = original_location
        customer.money -= customer.trip_cost(cheapest_shop, fuel)
        print(f"{customer.name} now has {round(customer.money, 2)} dollars")
        print("")
