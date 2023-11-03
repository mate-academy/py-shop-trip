from datetime import datetime
import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = []
    shops = []

    with open("config.json", "r") as config:
        data = json.load(config)

    fuel_price = data["FUEL_PRICE"]

    for customer in data["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"],
                fuel_price
            )
        )

    for shop in data["shops"]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    for customer in customers:
        dict_shops = {}
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            ox = shop.location[0]
            oy = shop.location[1]
            cost_fuel_trip = round(2 * customer.cost_fuel(ox, oy), 2)
            cost_products = customer.cost_products(shop.products)
            cost_trip = cost_fuel_trip + cost_products

            print(f"trip to {shop.name} ==>{cost_trip}")

            dict_shops[cost_trip] = [
                shop.name,
                customer.text_cost_products,
                shop.location[0],
                shop.location[1]
            ]

        min_cost = min(dict_shops.keys())

        if customer.money < min_cost:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            break

        print(f"{customer.name} rides to {dict_shops[min_cost][0]}\n")

        ox = dict_shops[min_cost][2]
        oy = dict_shops[min_cost][3]
        customer.position(ox, oy)

        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"DATE: {current_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        print(f"{dict_shops[min_cost][1]}")
        print("See you again!\n")

        print(f"{customer.name} rides home")
        ox = customer.location_home[0]
        oy = customer.location_home[1]
        customer.position(ox, oy)
        remain_money = round(customer.money - min_cost, 2)
        print(f"{customer.name} now has {remain_money} dollars\n")


shop_trip()
