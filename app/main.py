import json

from app.shop import Shop
from app.customer import Customer
from app.fuel_price import FuelPrice


def shop_trip() -> None:
    with open("app/config.json", "r") as data_file:
        data_file_json = json.load(data_file)
        fuel_price = FuelPrice(data_file_json)
        customers_list = [
            Customer(customer) for customer in data_file_json["customers"]
        ]

        shop_list = [
            Shop(shop) for shop in data_file_json["shops"]
        ]

        for shopper in customers_list:
            print(f"{shopper.name} has {shopper.money} dollars")

            dict_shop = {}
            for shop in shop_list:
                cost_to_shop = shopper.full_cost(
                    shop,
                    fuel_price
                )
                dict_shop[cost_to_shop] = shop
                print(f"{shopper.name}'s trip to the {shop.name} "
                      f"costs {cost_to_shop}")

            list_of_trip_costs = [cost for cost in dict_shop]
            min_amount = min(list_of_trip_costs)

            if shopper.money >= min_amount:
                shopper.shopping(
                    dict_shop[min_amount],
                    fuel_price
                )
            else:
                print(f"{shopper.name} doesn't have "
                      f"enough money to make purchase in any shop")
