import json
import datetime
import math


from app.customers import customer_list
from app.shops import shop_list


def shop_trip() -> None:
    with open(
            "py-shop-trip/app/config.json", "r"
    ) as json_file:
        customers_data = json.load(json_file)

    for customer in customer_list():

        print(f"{customer.name} has {customer.money} dollars")
        less_cost = {}
        shop_dict = {}
        for shop in shop_list():
            shop_name = {f"{shop.name}": {None}}
            total_cost_of_milk = shop.cost_of_milk * customer.amount_of_milk
            total_cost_of_bread = shop.cost_of_bread * customer.amount_of_bread
            total_cost_of_butter = (
                shop.cost_of_butter * customer.amount_of_butter
            )
            total_cost = (
                total_cost_of_milk + total_cost_of_bread
                + total_cost_of_butter
            )
            distance = math.dist(customer.location, shop.location)
            costs_trip = (
                round(((2 * distance * customer.car_fuel_consumption) / 100
                       * customers_data["FUEL_PRICE"] + total_cost), 2)
            )

            shop_name[shop.name] = {"total_cost_of_milk": total_cost_of_milk}
            shop_name[shop.name].update(
                {"total_cost_of_bread": total_cost_of_bread}
            )
            shop_name[shop.name].update(
                {"total_cost_of_butter": total_cost_of_butter}
            )
            shop_name[shop.name].update(
                {"total_cost": total_cost}
            )
            shop_name[shop.name].update(
                {"costs_trip": costs_trip}
            )
            print(
                f"{customer.name}'s trip to the {shop.name} costs {costs_trip}"
            )
            less_cost.update({costs_trip: shop.name})
            shop_dict.update(shop_name)
        cheapest = shop_dict[less_cost[min(less_cost.keys())]]
        if cheapest["costs_trip"] <= customer.money:

            print(
                f"{customer.name} rides "
                f"to {less_cost[min(less_cost.keys())]}"
            )

            print("")
            print(
                f"Date:"
                f" {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            )
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")
            print(
                f"{customer.amount_of_milk} milks "
                f"for {cheapest['total_cost_of_milk']} dollars"
            )

            print(
                f"{customer.amount_of_bread} breads "
                f"for {cheapest['total_cost_of_bread']} dollars"
            )
            print(
                f"{customer.amount_of_butter} butters "
                f"for {cheapest['total_cost_of_butter']} dollars"
            )
            print(f"Total cost is {cheapest['total_cost']} dollars")
            print("See you again!")
            print("")
            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now "
                f"has {round(customer.money - cheapest['costs_trip'], 2)} "
                f"dollars"
            )
            print("")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make purchase in any shop"
            )
