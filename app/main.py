import json
import datetime


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
        distance = (x_coord + y_coord) ** 0.5
        fuel_for_trip = (distance * (fuel_consumption / 100)) * 2
        price_for_fuel = round((fuel_for_trip * fuel_price), 2)
        fuel_prices.update({shop["name"]: price_for_fuel})
    return fuel_prices


def calculate_products(
        shops: list[dict],
        person: dict
):
    cart_price_in_shops = {}
    cart_prices = 0
    calc_product = []
    cart_all_product = {}
    for shop in shops:
        for product_name, product_count in person["product_cart"].items():
            price_one_product = shop["products"][product_name] * product_count
            cart_prices += price_one_product
            calc_product.append(
                [product_count,
                 product_name,
                 price_one_product]
            )

        cart_all_product.update({shop['name']: calc_product})
        calc_product = []
        cart_price_in_shops.update({shop["name"]: cart_prices})
        cart_prices = 0

    return cart_price_in_shops, cart_all_product


def calculate_trip_to_shop(
        person: dict,
        shops: list[dict],
        fuel_price: float,
        fuel_consumption: float,
):
    trip_to_shop = {}
    fuel = calculate_fuel(person, shops, fuel_price, fuel_consumption)
    products = calculate_products(shops, person)[0]

    for markets in shops:

        trip_price = round(
            fuel[markets["name"]] + products[markets["name"]], 2
        )
        trip_to_shop.update({markets["name"]: trip_price})
    return trip_to_shop


def shopping(
        customer: dict,
        shops: list[dict],
        fuel_price,
        fuel_consumption
):
    calc_products = calculate_products(shops, customer)
    trip_price = calculate_trip_to_shop(
        customer,
        shops,
        fuel_price,
        fuel_consumption
    )
    print(f"{customer['name']} has {customer['money']} dollars")
    lowest_prise = min(trip_price.values())
    lowest_price_shop = None

    for shop in shops:
        print(f"{customer['name']}'s trip to the {shop['name']} "
              f"costs {trip_price[shop['name']]}")
        if lowest_prise == trip_price[shop['name']]:
            lowest_price_shop = shop["name"]

    if customer["money"] < lowest_prise:
        print(f"{customer['name']} doesn't have enough money "
              f"to make purchase in any shop")

    else:
        date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{customer['name']} rides to {lowest_price_shop}\n")
        print(f"Date: {date_time}")
        print(f"Thanks, {customer['name']}, for you purchase!")
        print("You have bought: ")

        for product_i in range(len(customer['product_cart'])):
            product = calc_products[1][lowest_price_shop][product_i]
            print(f"{product[0]} {product[1]}s for {product[2]} dollars")

        print(f"Total cost is {calc_products[0][lowest_price_shop]} dollars")
        print("See you again!\n")
        print(f"{customer['name']} rides home")
        print(f"{customer['name']} now has"
              f" {customer['money'] - lowest_prise} dollars\n")


def shop_trip():
    with open("app/config.json", "r") as cfg:
        config = json.load(cfg)
        fuel_price = config["FUEL_PRICE"]
        customers = config["customers"]
        shops = config["shops"]

        for person in customers:
            fuel_consumption = person["car"]["fuel_consumption"]
            shopping(person, shops, fuel_price, fuel_consumption)


if __name__ == '__main__':
    shop_trip()
