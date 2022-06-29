import json
import datetime
import math


def shop_trip():
    with open('app/config.json', 'r') as file:
        shop_data = json.load(file)
    fuel_prise = shop_data['FUEL_PRICE']
    customers = shop_data['customers']
    shops = shop_data['shops']
    total_cost = {}
    dict_product = {}

    for customer in customers:
        print(f"{customer['name']} has {customer['money']} dollars")

        for shop in shops:
            distance = math.dist(customer["location"], shop["location"])
            fuel_consumption = customer["car"]["fuel_consumption"]
            cost_trip = (fuel_consumption * distance) / 100 * fuel_prise

            product_cost = {
                f"{customer['product_cart'][key]} {key}s":
                    customer["product_cart"][key] * values
                for key, values in shop["products"].items()}

            costs_shop = round(2 * cost_trip + sum(product_cost.values()), 2)
            print(f"{customer['name']}'s trip to the {shop['name']} \
            costs {costs_shop}")

            dict_product[shop['name']] = {"product": product_cost}
            total_cost[shop['name']] = costs_shop

        cheap_shop = min(total_cost, key=total_cost.get)

        if customer['money'] < min(total_cost.values()):
            print(f"{customer['name']} doesn't have enough money \
            to make purchase in any shop")
            break

        print(f"{customer['name']} rides to {cheap_shop}\n")

        time_now = datetime.datetime.now()
        time = time_now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time}\n"
              f"Thanks, {customer['name']}, for you purchase!\n"
              f"You have bought:")
        for key, values in dict_product[cheap_shop]['product'].items():
            print(f"{key} for {values }dollars")

        print(
            f"Total cost is {sum(dict_product[cheap_shop]['product'].values())}\
             dollars\n"
            f"See you again!\n\n"
            f"{customer['name']} rides home\n"
            f"{customer['name']} now has \
            {customer['money'] - total_cost[cheap_shop]} dollars\n")
