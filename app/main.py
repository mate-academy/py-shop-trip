import json
import math
import datetime


def shop_trip():
    with open("app/config.json", "r") as data_json:
        user_data = json.load(data_json)

    fuel_price_data = user_data["FUEL_PRICE"]
    customers_data = user_data["customers"]
    shops_data = user_data["shops"]

    for customer in customers_data:
        print(f"{customer['name']} has {customer['money']} dollars")
        overall_prices = price_for_trip(customer, shops_data, fuel_price_data)

        for shop, overall_price in overall_prices.items():
            print(f"{customer['name']}'s trip to the {shop} "
                  f"costs {round(overall_price, 2)}")
        cheapest_shop = min(overall_prices, key=overall_prices.get)

        if customer["money"] >= overall_prices[cheapest_shop]:
            print(f"{customer['name']} rides to {cheapest_shop}\n")

            initial_location = customer["location"]

            for shop in shops_data:
                if shop["name"] == cheapest_shop:
                    customer["location"] = shop["location"]
                    print_invoice(customer, shop)

            customer["location"] = initial_location
            cash = customer["money"] - overall_prices[cheapest_shop]
            print(f"{customer['name']} rides home\n"
                  f"{customer['name']} now has {round(cash, 2)} dollars\n")

        else:
            print(f"{customer['name']} doesn't have "
                  "enough money to make purchase in any shop")


def price_for_fuel(customer, shop, fuel_price):
    fuel_consumption = customer["car"]["fuel_consumption"] / 100
    distance = math.dist(customer["location"], shop["location"])
    fuel_cost = fuel_price * fuel_consumption * (distance * 2)

    return fuel_cost


def price_for_trip(customer, shops, fuel_price):
    price_trip = {}
    for shop in shops:
        price_trip[shop["name"]] = price_for_fuel(customer, shop, fuel_price)
        for product, amount in customer["product_cart"].items():
            price_trip[shop["name"]] += shop["products"][product] * amount

    return price_trip


def print_invoice(customer, shop):
    invoice = 0
    print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
    print(f"Thanks, {customer['name']}, for you purchase!")
    print("You have bought: ")
    for quantity, price in customer["product_cart"].items():
        purchase = shop["products"][quantity] * price
        print(f"{price} {quantity}s for {purchase} dollars")
        invoice += purchase

    print(f"Total cost is {invoice} dollars\n"
          "See you again!")
    print()


if __name__ == "__main__":
    shop_trip()
