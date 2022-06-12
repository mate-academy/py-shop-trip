import json
import math
import datetime

with open("app/config.json") as f:
    data = json.load(f)
    fuel_price = data['FUEL_PRICE']
    customers = data['customers']
    shops = data['shops']


def products_cost(prod_cart: dict, prod_shop: dict):
    total = 0
    for key, value in prod_cart.items():
        total += value * prod_shop[key]
    return total


def fuel_cost(first: list, second: list, fuel_cons: float):
    distance = math.dist(first, second)
    cost = (distance / 100) * fuel_cons * fuel_price
    return round(cost * 2, 2)


def print_receipt(prod_cart: dict, prod_shop: dict, name: str):
    print(
        f"\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"Thanks, {name}, for you purchase!\n"
        f"You have bought: "
    )
    for prod, quan in prod_cart.items():
        print(f"{quan} {prod}s for {quan * prod_shop[prod]} dollars")
    print(f"Total cost is {products_cost(prod_cart, prod_shop)} "
          f"dollars\nSee you again!\n")


def shop_trip():
    for person in customers:
        money = person['money']
        print(f"{person['name']} has {money} dollars")
        totals = []
        for shop in shops:
            total_cost = fuel_cost(
                person['location'],
                shop['location'],
                person['car']['fuel_consumption'])\
                + products_cost(person["product_cart"], shop["products"])
            totals.append(total_cost)
            print(f"{person['name']}'s trip to "
                  f"the {shop['name']} costs {total_cost}")

        if min(totals) > money:
            print(f"{person['name']} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            best = shops[totals.index(min(totals))]['name']
            products = shops[totals.index(min(totals))]['products']
            print(f"{person['name']} rides to {best}")
            print_receipt(person['product_cart'], products, person['name'])
            print(f"{person['name']} rides home\n{person['name']} "
                  f"now has {money - min(totals)} dollars\n")
