import json
from datetime import datetime


# 9.9 -- розхід на 100 км | customer_coords(12, -2), shop_cooord(10, -5) | 2.4 -- Сумма за 1 літр
# (12 - 10) ** 2  + (-2 - -5) ** 2 == 2 ** 2 + 3 ** 2 = 13 -- відстань
# 9.9 / 100 = 0.099 -- розхід на 1 км
# 13 * 0.099 == 1.287 -- розхід на 13 км
# 1.287 * 2.4 = 3.0888 -- ціна поїздки до магазину

def calculate_fuel(
        person: dict,
        shops: list[dict],
        fuel_price: float,
        fuel_consumption: float,
):
    fuel_prices = {}
    for shop in shops:
        x_coord = ((person["location"][0] - shop["location"][0]) ** 2)
        y_coord = ((person["location"][1] - shop["location"][1]) ** 2)
        distance = x_coord + y_coord
        fuel_for_trip = round((distance * (fuel_consumption / 100)) * 2, 2)
        price_for_fuel = round((fuel_for_trip * fuel_price), 2)
        fuel_prices.update({shop["name"]: price_for_fuel})
    return fuel_prices


def calculate_products(
        shops: list[dict],
        person: dict
):
    cart_price_in_shops = {}
    cart_prices = 0

    for shop in shops:
        for product_name, product_count in person["product_cart"].items():
            price_one_product = shop["products"][product_name] * product_count
            cart_prices += price_one_product

        cart_price_in_shops.update({shop["name"]: cart_prices})
        cart_prices = 0

    return cart_price_in_shops


def calculate_trip_to_shop(
        person: dict,
        shops: list[dict],
        fuel_price: float,
        fuel_consumption: float,
):
    trip_to_shop = {}
    fuel = calculate_fuel(person, shops, fuel_price, fuel_consumption)
    products = calculate_products(shops, person)

    for markets in shops:

        trip_price = round(fuel[markets["name"]] + products[markets["name"]], 2)
        trip_to_shop.update({markets["name"]: trip_price})
    return trip_to_shop


def shopping(
        customer: dict,
        shops: list[dict],
        trip_price: dict,
):
    print(f"{customer['name']} has {customer['money']} dollars")
    lowest_prise = min(trip_price.values())
    shop_name_with_lowest_price = None

    for i in range(len(shops)):
        print(f"{customer['name']}'s trip to {shops[i]['name']} costs {trip_price[shops[i]['name']]}")

        if lowest_prise == trip_price[shops[i]['name']]:
            shop_name_with_lowest_price = shops[i]["name"]

    if customer["money"] < lowest_prise:
        print(f"{customer['name']} doesn't have enough money to make purchase in any shop")

    else:
        print(f"{customer['name']} rides to {shop_name_with_lowest_price}\n")
        print(datetime.now().strftime("Date: %y/%m/%d %H:%M:%S"))
        print(f"Thanks, {customer['name']}, for you purchase!")
        print("You have bought:")
        # In this line must be block of code :)
        # But i need a help with correct values in the function calculate_fuel
        print(f"Total cost is {calculate_products(shops, customer)[shop_name_with_lowest_price]} dollars")
        print("See you again!")
        print(f"{customer['name']} rides home")
        print(f"{customer['name']} now has {customer['money'] - lowest_prise} dollars\n")


def shop_trip():
    with open("config.json", "r") as cfg:
        config = json.load(cfg)
        fuel_price = config["FUEL_PRICE"]
        customers = config["customers"]
        shops = config["shops"]

        for person in customers:
            fuel_consumption = person["car"]["fuel_consumption"]
            shopping(person, shops, calculate_trip_to_shop(person, shops, fuel_price, fuel_consumption))


if __name__ == '__main__':
    shop_trip()
