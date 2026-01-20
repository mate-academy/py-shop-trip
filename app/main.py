import json
import datetime

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        all_info = json.load(file)
        fuel_price = all_info["FUEL_PRICE"]
        customer_info = all_info["customers"]
        shop_info = all_info["shops"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(**customer["car"]),
        )
        for customer in customer_info
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in shop_info
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trips = {}

        for shop in shops:
            product_cost = shop.calculate_purchase(customer.product_cart)
            fuel_cost = customer.car.calculate_road_cost(
                customer.location, shop.location, fuel_price
            )
            trip_cost = round(product_cost + fuel_cost, 2)
            trips[trip_cost] = shop
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )

        if customer.money < min(trips.keys()):
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        min_purchase_cost = min(trips.keys())
        chosen_shop = trips[min_purchase_cost]
        print(f"{customer.name} rides to {chosen_shop.name}\n" f"")
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        for product_name, amount in customer.product_cart.items():
            products_cost = amount * chosen_shop.products[product_name]
            print(f"{amount} {product_name}s for {products_cost} dollars")

        print(
            f"Total cost is "
            f"{chosen_shop.calculate_purchase(customer.product_cart)} dollars"
        )
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - min_purchase_cost} dollars\n")
