import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("D:\\projects1\\py-shop-trip\\app\\config.json", "r") \
            as data_file:
        data_file_json = json.load(data_file)

        customers_list = []
        for customer in data_file_json["customers"]:
            customers_list.append(Customer(customer))
        shop_list = []
        for shop in data_file_json["shops"]:
            shop_list.append(Shop(shop))

        for shopper in customers_list:
            print(f"{shopper.name} has {shopper.money} dollars")
            dict_shop = {}
            for shop in shop_list:
                cost_to_shop = shopper.full_cost(
                    shop,
                    data_file_json["customers"]["car"],
                    data_file_json["FUEL_PRICE"]
                )
                dict_shop[cost_to_shop] = shop
                print(f"{shopper.name}'s trip to the {shop.name} "
                      f"cost {cost_to_shop}")

            list_of_trip_costs = [cost for cost in dict_shop]
            min_amount = list_of_trip_costs[0]
            for amount in dict_shop:
                if amount < min_amount:
                    min_amount = amount

            if shopper.money >= min_amount:
                shopper.shopping(
                    shop,
                    data_file_json["customers"]["car"],
                    data_file_json["FUEL_PRICE"]
                )
            print(f"{shopper.name} doesn't have "
                  f"enough money to make purchase in any shop")
