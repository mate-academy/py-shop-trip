import json
from math import sqrt
from datetime import datetime


def shop_trip():
    with open("app/config.json") as f:
        info = json.load(f)
    for person in info["customers"]:
        print(f"{person['name']} has {person['money']} dollars")
        min_ = 1000000
        for shop in info["shops"]:
            list_cost = cost_of_products(person, shop)
            need_money = sum(list_cost) + cost_of_fuel(person, shop, info)
            print(f"{person['name']}'s trip to the"
                  f" {shop['name']} costs {need_money}")
            if min_ > need_money:
                min_ = need_money
                min_list_cost = list_cost
                name_shop = shop["name"]
        if person["money"] > min_:
            print_check(person, name_shop, min_list_cost)
            print(f"{person['name']} rides home\n"
                  f"{person['name']} now has "
                  f"{person['money'] - min_} dollars\n")
        else:
            print(f"{person['name']} doesn't have"
                  f" enough money to make purchase in any shop")


def cost_of_products(person, shop):
    products = person["product_cart"]
    cost_product = shop["products"]
    sum_ = []
    for product in products:
        sum_.append(products[product] * cost_product[product])

    return sum_


def cost_of_fuel(person, shop, info):
    home_location = person["location"]
    shop_location = shop["location"]
    x = (home_location[0] - shop_location[0]) ** 2
    y = (home_location[1] - shop_location[1]) ** 2
    distance = (sqrt(x + y)) * 2
    fuel = person["car"]["fuel_consumption"] / 100
    cost = (fuel * distance) * info["FUEL_PRICE"]
    return round(cost, 2)


def print_check(person, name_shop, min_list_cost):
    print(f"{person['name']} rides to {name_shop}\n\n"
          f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
          f"Thanks, {person['name']}, for you purchase!\n"
          f"You have bought: \n"
          f"{person['product_cart']['milk']} milks"
          f" for {min_list_cost[0]} dollars\n"
          f"{person['product_cart']['bread']} breads"
          f" for {min_list_cost[1]} dollars\n"
          f"{person['product_cart']['butter']} butters"
          f" for {min_list_cost[2]} dollars\n"
          f"Total cost is {sum(min_list_cost)} dollars\n"
          f"See you again!\n"
          )
