# import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.data import data


def shop_trip() -> None:
    fuel_price = data["FUEL_PRICE"]

    customers = [
        Customer(customer["name"], customer["money"], customer["location"],
                 Car(customer["car"]["brand"],
                     customer["car"]["fuel_consumption"],
                     customer["location"]), customer["product_cart"])
        for customer in data["customers"]]

    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shopping = customer.find_the_cheapest_shopping(
            shops, fuel_price)

        if cheapest_shopping[1] <= customer.money:
            customer.make_shopping(cheapest_shopping[0], fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money to "
                  + "make a purchase in any shop")
