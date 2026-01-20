import json
import datetime

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        file_data = json.load(file)
    fuel_price = file_data["FUEL_PRICE"]

    _customers = file_data["customers"]
    customers = [
        Customer(
            name=i["name"],
            products=i["product_cart"],
            location=i["location"],
            money=i["money"],
            car=Car(
                brand=i["car"]["brand"],
                fuel_consumption=i["car"]["fuel_consumption"]
            )
        ) for i in _customers
    ]
    _shops = file_data["shops"]

    shops = [Shop(**shop) for shop in _shops]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_total_cost = float("inf")
        best_product_price = 0
        best_shop = None
        for shop in shops:
            distance = customer.calculate_distance(shop)
            product_price = 0
            for product, quantity in customer.products.items():
                if product in shop.products:
                    product_price += shop.products[product] * quantity
            trip_cost = customer.car.fuel_consumption * distance * fuel_price
            total_cost = product_price + round(trip_cost / 100 * 2, 2)
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {total_cost}")
            if total_cost < best_total_cost:
                best_total_cost = total_cost
                best_shop = shop
                best_product_price = product_price

        if best_total_cost <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}\n")
            print(f"Date:"
                  f" {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer.products.items():
                cost = best_shop.products[product] * quantity
                cost = float(cost)
                _cost = f"{int(cost)}" if cost.is_integer() else f"{cost:.1f}"
                print(f"{quantity} {product}s for {_cost} dollars")

            print(f"Total cost is {best_product_price} dollars"
                  f"\nSee you again!\n")

            money_left = customer.money - best_total_cost
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {money_left} dollars\n")
        else:
            print(f"{customer.name}"
                  f" doesn't have enough money to make a purchase in any shop")
