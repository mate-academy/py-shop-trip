import json
import pathlib


def shop_trip():
    data = parse_data()
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    for customer in customers:
        print(f"{customer['name']} has {customer['money']} dollars")

        shop, cost_of_way = choose_the_most_profitable_way(
            customer,
            shops,
            fuel_price
        )
        if not shop:
            continue
        print(f"Date: 11/03/2020 13:15:34")
        print(f"Thanks, {customer['name']}, for you purchase!")
        bought_products(customer["product_cart"], shop["products"])

        print(f"{customer['name']} rides home\n"
              f"{customer['name']} now has "
              f"{customer['money'] - cost_of_way:.2f} dollars\n")


def parse_data():
    BASE_DIR = pathlib.Path(__file__).resolve().parent
    with open(BASE_DIR / "config.json", "r") as f:
        data = json.load(f)
    return data


def choose_the_most_profitable_way(customer, shops, fuel_price):
    costs_of_ways = {}
    fuel_consumption = customer["car"]["fuel_consumption"]
    product_cart = customer["product_cart"]
    for shop in shops:
        distance = get_distance(customer, shop)
        fuel_cost = distance * fuel_price * fuel_consumption / 100 * 2
        cost_of_cart = sum(
            amount * shop["products"][product]
            for product, amount in product_cart.items()
        )
        cost_of_way = fuel_cost + cost_of_cart
        costs_of_ways[shop["name"]] = cost_of_way
        print(f"{customer['name']}'s trip to the {shop['name']} "
              f"costs {cost_of_way:.2f}")

    shop_name = min(costs_of_ways, key=costs_of_ways.get)

    if costs_of_ways[shop_name] > customer["money"]:
        print(f"{customer['name']} doesn't have enough money "
              f"to make purchase in any shop")
        return False, False
    print(f"{customer['name']} rides to {shop_name}\n")
    for shop in shops:
        if shop["name"] == shop_name:
            return shop, costs_of_ways[shop_name]


def get_distance(customer, shop):
    x_customer = customer["location"][0]
    y_customer = customer["location"][1]
    x_shop = shop["location"][0]
    y_shop = shop["location"][1]
    return ((x_shop - x_customer) ** 2 + (y_shop - y_customer) ** 2) ** 0.5


def bought_products(product_cart, product_prices):
    print("You have bought: ")
    sum = 0
    for product, amount in product_cart.items():
        price = amount * product_prices[product]
        print(f"{amount} {product}s for {price} dollars")
        sum += price
    print(f"Total cost is {sum} dollars\n"
          f"See you again!\n")


shop_trip()
