import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop
from app import utils


def shop_trip() -> None:
    # Відкриваю файл і перетворюю в словник
    with open("app/config.json", "r") as jsonf:
        j_dict = json.load(jsonf)
    fuel_price = j_dict["FUEL_PRICE"]

    customer_list = []
    shop_list = []

    # Створюю об'єкти Клієнта і магазина
    for customer in j_dict["customers"]:
        customer_list.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                    )
            ))

    for shop in j_dict["shops"]:
        shop_list.append(Shop(shop["name"],
                              shop["location"],
                              shop["products"]))

    # Основна частина
    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        trip_prices = []
        for shop in shop_list:
            calculations = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {calculations}")
            if (shop.has_all_products(customer.product_cart)
                    and customer.can_afford_trip(shop, fuel_price)):
                trip_prices.append((shop, calculations))
        if not trip_prices:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        best_shop, _ = min(trip_prices, key=lambda pair: pair[1])
        customer.go_to(best_shop, fuel_price)
        print()
        customer.buy_products(best_shop)
        customer.print_receipt(best_shop)
        print()
        customer.go_home(fuel_price)
        print(f"{customer.name} now has "
              f"{utils.round2(customer.money)} dollars")
        print()
