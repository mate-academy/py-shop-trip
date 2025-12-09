import json
from pathlib import Path
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip():
    config_path = Path(__file__).resolve().parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = [Shop(shop["name"], shop["location"], shop["products"])
            for shop in data["shops"]]

    customers = []
    for c in data["customers"]:
        car = Car(c["car"]["brand"], c["car"]["fuel_consumption"])
        customer = Customer(c["name"], c["product_cart"], c["location"], c["money"], car)
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            total_cost = customer.count_total_trip_cost(shop, fuel_price)
            if total_cost is None:
                print(f"{customer.name} can't buy all products in {shop.name}")
            print(f"{customer.name}'s trip to the {shop.name} costs {total_cost:.2f}")

        cheapest_shop = None
        cheapest_cost = None

        for shop in shops:
            total_cost = customer.count_total_trip_cost(shop, fuel_price)
            if total_cost is None:
                continue

            if cheapest_cost is None or total_cost < cheapest_cost:
                cheapest_shop = shop
                cheapest_cost = total_cost

        if cheapest_shop and customer.money >= cheapest_cost:
            customer.buy_products(cheapest_shop, fuel_price)
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


try_one = shop_trip()
print(try_one)