import json
from math import hypot

with open("app/config.json", "r") as config_file:
    info = json.load(config_file)

FUEL_PRICE = info["FUEL_PRICE"]
CUSTOMERS = info["customers"]
SHOPS = info["shops"]


def make_choice(customer, shops):
    list_cost = cost_products_list(customer, shops)
    travel_cost = cost_get_to_shop(customer, shops)
    min_cost = float('inf')
    choice = ""
    for shop in travel_cost:
        if shop in list_cost:
            cost_of_trip = list_cost[shop][0] + travel_cost[shop]
            print(f"{customer['name']}'s trip to the {shop} "
                  f"costs {cost_of_trip}")
            if cost_of_trip < min_cost:
                min_cost = cost_of_trip
                choice = shop
    if min_cost > customer["money"]:
        return
    else:
        return choice


def cost_get_to_shop(customer, shops):
    customer_point = customer["location"]
    x1, y1 = customer_point[0], customer_point[1]
    consumption = customer["car"]["fuel_consumption"]
    travel_cost = {}
    for shop in shops:
        x2, y2 = shop["location"][0], shop["location"][1]
        distance = round(hypot(x2 - x1, y2 - y1), 2)
        fuel_per_km = round(consumption * FUEL_PRICE / 100, 2)
        cost = round(fuel_per_km * distance, 2)
        travel_cost[f"{shop['name']}"] = cost * 2
    return travel_cost


def cost_products_list(customer, shops):
    product_cart = customer["product_cart"]
    list_cost = {}
    for shop in shops:
        products = shop["products"]
        sum_cost_products = 0
        shopping_list = {product: 0 for product in product_cart}
        for product in product_cart:
            if product in products:
                shopping_list[product] += round(
                    product_cart[product] * products[product], 2)
                sum_cost_products += round(
                    product_cart[product] * products[product], 2)
        list_cost[f"{shop['name']}"] = round(
            sum_cost_products, 2), shopping_list
    return list_cost
