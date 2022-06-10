import json

import datetime

from math import sqrt


def shop_trip():

    with open("app/config.json") as data_file:
        users_data = json.load(data_file)

    fuel_price = users_data["FUEL_PRICE"]
    customers = users_data["customers"]
    shops = users_data["shops"]

    for customer in customers:
        print(f"{customer['name']} has {customer['money']} dollars")
        overall_prices = []

        for shop in shops:
            trip_coast = trip_to_shop(customer, shop, fuel_price)
            print(f"{customer['name']}'s trip to the "
                  f"{shop['name']} costs {trip_coast[0]}")

            overall_prices.append(trip_coast)

        min_price, chosen_shop = min(overall_prices)

        if customer['money'] > min_price:
            print(f"{customer['name']} rides to {chosen_shop['name']}\n")
            home = customer['location']
            customer['location'] = chosen_shop["location"]
            shop_prints_purchase_receipt(customer, chosen_shop)
            print(f"{customer['name']} rides home")
            customer['location'] = home
            left_money = customer['money'] - min_price
            print(f"{customer['name']} now has {left_money} dollars")

        else:
            print(f"{customer['name']} doesn't have enough money to make purchase in any shop")

        if int(customers.index(customer)) < len(customers) - 1:
            print()


def trip_to_shop(customer, shop, fuel_price):

    x_customer, y_customer, = customer["location"]
    x_shop, y_shop, = shop["location"]
    expenditure = customer["car"]["fuel_consumption"]

    x_difference = x_customer - x_shop
    y_difference = y_customer - y_shop

    distance = round(sqrt(x_difference ** 2 + y_difference ** 2), 2)
    fuel_cost = round((fuel_price * expenditure) / 100, 2)
    cost_for_road = round(distance * fuel_cost, 2)

    price_for_products = 0

    for product_buy in customer["product_cart"]:
        for product_sell in shop["products"]:
            if product_buy == product_sell:
                price_for_products += customer["product_cart"][product_buy] * \
                                      shop["products"][product_sell]

    trip_coast = round(cost_for_road * 2 + price_for_products, 2)

    return [trip_coast, shop]


def shop_prints_purchase_receipt(customer, shop):

    now_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(f"Date: {now_date}")
    print(f"Thanks, {customer['name']}, for you purchase!")
    print("You have bought: ")

    cost_of_products = 0

    for product_buy in customer["product_cart"]:
        for product_sell in shop["products"]:
            if product_buy == product_sell:
                count = customer['product_cart'][product_buy]
                coast = customer['product_cart'][product_buy] * \
                    shop["products"][product_sell]
                print(f"{count} {product_buy}s for {coast} dollars")
                cost_of_products += customer["product_cart"][product_buy] * \
                    shop["products"][product_sell]

    print(f"Total cost is {cost_of_products} dollars")
    print("See you again!")

    return cost_of_products


if __name__ == '__main__':
    shop_trip()
