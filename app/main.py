import json
import math
import datetime

with open("app/config.json") as json_input:
    data = json.load(json_input)
FUEL_PRICE = data["FUEL_PRICE"]


def shop_trip():
    with open("app/config.json") as json_input_file:
        data = json.load(json_input_file)
    shops = data["shops"]
    for customer in data["customers"]:
        riding_to_the_store(customer, shops)


def get_distance(customer: dict, shop: dict):
    distance = math.dist(customer["location"], shop["location"])
    return distance


def get_cost_of_ride_to_the_store(customer: dict, shop: dict):
    distance = get_distance(customer, shop)
    need_fuel = ((customer["car"]["fuel_consumption"] / 100) * distance)
    fuel_cost = need_fuel * FUEL_PRICE
    products_cost = 0
    for keys, values in customer["product_cart"].items():
        cost = values * shop["products"][keys]
        products_cost += cost
    return round(fuel_cost * 2 + products_cost, 2)


def riding_to_the_store(customer: dict, shops: list):
    name = customer["name"]
    money = customer["money"]
    print(f"{name} has {money} dollars")
    cost_of_purchases = []
    stores = {}
    for shop in shops:
        shop_name = shop["name"]
        cost = get_cost_of_ride_to_the_store(customer, shop)
        cost_of_purchases.append(cost)
        stores[shop_name] = cost
        print(f"{name}'s trip to the {shop_name} costs {cost}")
    cheapest_store = min(stores, key=stores.get)
    for shop in shops:
        if shop["name"] == cheapest_store:
            cheapest_store = shop
    if money >= min(cost_of_purchases):
        print(f"{name} rides to {cheapest_store['name']}\n")
        purchase_in_the_store(customer, cheapest_store)
    else:
        print(f"{name} doesn't have enough money to make purchase in any shop")


def purchase_in_the_store(customer: dict, shop: dict):
    name = customer["name"]
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d/%m/%Y %H:%M:%S")
    money = customer["money"]
    print(f"Date: {formatted_time}")
    print(f"Thanks, {name}, for you purchase!")
    cost_of_all_product = 0
    print("You have bought: ")
    for product, product_cost in shop["products"].items():
        product_amount = customer["product_cart"][product]
        total_cost_of_product = product_cost * product_amount
        print(f"{product_amount} {product}s for"
              f" {total_cost_of_product} dollars")
        cost_of_all_product += total_cost_of_product
    distance = get_distance(customer, shop)
    need_fuel = ((customer["car"]["fuel_consumption"] / 100) * distance)
    fuel_cost = need_fuel * FUEL_PRICE
    money_left = round(money - cost_of_all_product - (fuel_cost * 2), 2)
    print(f"Total cost is {cost_of_all_product} dollars")
    print("See you again!\n")
    print(f"{name} rides home")
    print(f"{name} now has {money_left} dollars\n")


shop_trip()
