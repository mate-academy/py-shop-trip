import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as data_in:
        data_from_file = json.load(data_in)
        fuel_coast = data_from_file["FUEL_PRICE"]
        customers = [
            Customer(customer) for customer in data_from_file["customers"]
        ]
        shops = [Shop(shop) for shop in data_from_file["shops"]]

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            dict_shop_and_coast = {}
            for shop in shops:
                coast_to_shop = customer.coast_of_trip_to_shop(
                    shop,
                    fuel_coast
                )
                dict_shop_and_coast[coast_to_shop] = shop
                print(f"{customer.name}'s trip to "
                      f"the {shop.name} costs {coast_to_shop}")

            list_of_trip_coasts = [key for key in dict_shop_and_coast]
            minimal_coast = list_of_trip_coasts[0]
            for coast in dict_shop_and_coast:
                if coast < minimal_coast:
                    minimal_coast = coast

            if customer.money >= minimal_coast:
                customer.go_shopping(
                    dict_shop_and_coast[minimal_coast],
                    fuel_coast
                )

            else:
                print(f"{customer.name} doesn't have enough"
                      f" money to make purchase in any shop")
