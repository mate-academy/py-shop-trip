import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        shop_info = json.load(file)

    fuel_price = shop_info["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"])
        for customer in shop_info["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"])
        for shop in shop_info["shops"]
    ]

    for customer in customers:
        customer.customer_balance_before()

        min_cost_trip = 10000000000
        name_shop = shops[0].name
        for shop in shops:
            count_fuel = (
                fuel_price * shop.calculation_distance_to_shop(customer)
                * 2 * customer.car["fuel_consumption"] / 100)
            cost_basket_products = \
                shop.calculation_cost_basket_products(customer)
            cost_trip_shop = round(
                count_fuel + cost_basket_products, 2)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {cost_trip_shop}")

            if min_cost_trip > cost_trip_shop:
                min_cost_trip = cost_trip_shop
                name_shop = shop.name
            if min_cost_trip <= customer.money:
                balance = round(customer.money - min_cost_trip, 2)
                print(f"{customer.name} rides to {name_shop}")
                Shop.what_customer_bought(shop, customer)
                print(f"{customer.name} rides home\n"
                      f"{customer.name} now has "
                      f"{balance} dollars")

            else:
                print(f"{customer.name} doesn't have "
                      f"enough money to make purchase in any shop")
