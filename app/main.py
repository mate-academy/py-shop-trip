import json
import os.path

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "config.json")
    with open(file_path, "r") as file:
        config = json.load(file)
        fuel_price = config.get("FUEL_PRICE")
    for customer_ in config.get("customers"):
        customer = Customer(customer_)
        print(f"{customer.name} has {customer.money} dollars")
        lowest_price = 0
        optimal_place = ""
        for shop_ in config.get("shops"):
            shop = Shop(shop_)
            cost_of_trip = shop.calculate_trip_price(customer, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {cost_of_trip}")
            if optimal_place == "":
                optimal_place = shop.name
                lowest_price = cost_of_trip
            if cost_of_trip < lowest_price:
                optimal_place = shop.name
                lowest_price = cost_of_trip
        if lowest_price > customer.money:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {optimal_place}\n")
        for shop_ in config.get("shops"):
            shop = Shop(shop_)
            if shop.name == optimal_place:
                shop.shop_receipt(customer)
                print(f"{customer.name} rides home\n"
                      f"{customer.name} now has "
                      f"{customer.money - lowest_price} dollars\n")
