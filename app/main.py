import datetime
import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    with open(path, "r") as config:
        data_from_json = json.load(config)

        customers = [
            Customer.get_info_from_json_file(customer_data)
            for customer_data in data_from_json["customers"]
        ]

        shops = [
            Shop.get_info_from_json_file(shop_data)
            for shop_data in data_from_json["shops"]
        ]

    for customer in customers:

        list_of_total_costs = []
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            total_cost = customer.calculate_fuel_cost(
                customer.calculate_distance_to_shop(shop.location),
                data_from_json["FUEL_PRICE"]
            )
            total_cost += customer.calculate_total_cost_in_shop(shop)
            list_of_total_costs.append(total_cost)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")

        if customer.money < min(list_of_total_costs):
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            min_value = min(list_of_total_costs)
            shop_index = list_of_total_costs.index(min_value)
            shop = shops[shop_index]

            print(f"{customer.name} rides to {shop.name}\n")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            customer.print_detailed_purchase_report(shop)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min_value} dollars\n")
