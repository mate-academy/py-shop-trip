import json

from datetime import datetime


from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        shopping_data = json.load(file)

    fuel_cost = shopping_data["FUEL_PRICE"]
    customer_list = [
        Customer(**customer, fuel_cost=fuel_cost)
        for customer in shopping_data["customers"]]

    shop_list = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in shopping_data["shops"]
    ]

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

            time_stamp = datetime.strptime(
                "04/01/2021 12:33:41", "%m/%d/%Y %H:%M:%S"
            )
            time_stamp = time_stamp.strftime("%m/%d/%Y %H:%M:%S")

            print(
                f"{customer.name} rides to {min_cost_trip_shop[0]}\n\n"
                f"Date: {time_stamp}\n"
                f"Thanks, {customer.name}, for your purchase!\n"
                "You have bought: "
            )

            for item, value in min_receipt_shop.items():
                if item != "total_prod_cost" and item != "shop_location":
                    if item == "bread":
                        print(f"{customer.product_list[item]} "
                              f"{item}s for {int(value)} dollars")
                    else:
                        print(f"{customer.product_list[item]} "
                              f"{item}s for {value} dollars")

            print(
                f"Total cost is {min_receipt_shop['total_prod_cost']} "
                f"dollars\n"
                "See you again!\n\n"
                f"{customer.name} rides home\n"
                f"{customer.name} now has "
                f"{customer.money - min_cost_trip_shop[1]} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
