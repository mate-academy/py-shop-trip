import datetime
import json


with open("app/config.json") as file:
    trip_info = json.load(file)

FUEL_PRICE = trip_info["FUEL_PRICE"]
CUSTOMERS = trip_info["customers"]
SHOPS = trip_info["shops"]


def fuel_cost(home: list, shop: list, fuel_consumption):
    distance = \
        round(((home[0] - shop[0]) ** 2 + (home[1] - shop[1]) ** 2) ** 0.5, 2)
    fuel_per_km = round(fuel_consumption * FUEL_PRICE / 100, 2)
    return round(fuel_per_km * distance, 2)


def products_cost(products: dict, prices: dict):
    return sum(products[key] * prices[key] for key in products)


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
        costs = []
        for i in range(3):
            fuel = fuel_cost(customer['location'],
                             SHOPS[i]['location'],
                             customer['car']['fuel_consumption'])
            purchases = products_cost(customer['product_cart'],
                                      SHOPS[i]['products'])
            cost_trip = fuel * 2 + purchases
            print(f"{customer['name']}'s trip to the {SHOPS[i]['name']} "
                  f"costs {round(cost_trip, 2)} ")
            costs.append(cost_trip)
        min_cost = min(costs)
        if min_cost <= customer['money']:
            print(f"{customer['name']} rides to "
                  f"{SHOPS[costs.index(min_cost)]['name']}\n")
            home = customer['location']
            customer['location'] = SHOPS[costs.index(min_cost)]['location']
            print_receipt(customer['name'],
                          customer['product_cart'],
                          SHOPS[costs.index(min_cost)]['products'])
            print(f"{customer['name']} rides home\n"
                  f"{customer['name']} now has "
                  f"{customer['money'] - min_cost} dollars\n")
            customer['location'] = home
        else:
            print(f"{customer['name']} doesn't have "
                  f"enough money to make purchase in any shop")


if __name__ == '__main__':
    shop_trip()
