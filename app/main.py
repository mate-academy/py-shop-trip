import datetime
import json


with open("app/config.json") as file:
    trip_info = json.load(file)

FUEL_PRICE = trip_info["FUEL_PRICE"]
CUSTOMERS = trip_info["customers"]
SHOPS = trip_info["shops"]


def fuel_cost(home: list, shop: list, fuel_consumption):
    distance = ((home[0] - shop[0]) ** 2 + (home[1] - shop[1]) ** 2) ** 0.5
    return round(fuel_consumption * distance / 100 * FUEL_PRICE, 2)


def products_cost(products: dict, prices: dict):
    return round(sum(products[key] * prices[key] for key in products), 2)


def print_receipt(name, products: dict, prices: dict):
    current = datetime.datetime.now()
    print(f"Date: {current.strftime('%m/%d/%Y, %H:%M:%S')}\nThanks, "
          f"{name}, for you purchase!\nYou have bought:")
    for key in products:
        print(f"{products[key]} {key}s for "
              f"{products[key] * prices[key]} dollars")
    print(f"Total cost is {products_cost(products, prices)}"
          f" dollars\nSee you again!")


def shop_trip():
    for customer in CUSTOMERS:
        print(f"{customer['name']} has {customer['money']} dollars")
        min_cost = 100
        cheapest_shop = 0
        shop_number = 0
        for i in range(3):
            fuel = fuel_cost(customer['location'],
                             SHOPS[i]['location'],
                             customer['car']['fuel_consumption'])
            purchases = products_cost(customer['product_cart'],
                                      SHOPS[i]['products'])
            cost_trip = fuel * 2 + purchases
            print(f"{customer['name']}'s trip to the {SHOPS[i]['name']} "
                  f"costs {round(cost_trip, 2)} ")
            if cost_trip < min_cost:
                min_cost = cost_trip
                cheapest_shop = SHOPS[i]['name']
                shop_number = i
        if min_cost <= customer['money']:
            print(f"{customer['name']} rides to {cheapest_shop}\n")
            print_receipt(customer['name'],
                          customer['product_cart'],
                          SHOPS[shop_number]['products'])
            print(f"{customer['name']} rides home\n"
                  f"{customer['name']} now has "
                  f"{customer['money'] - min_cost} dollars\n")
        else:
            print(f"{customer['name']} doesn't have "
                  f"enough money to make purchase in any shop")


shop_trip()
