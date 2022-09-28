import json
from math import dist
from app.customers import Customer
from app.car import Car
from app.shop import Shop


def shop_trip():

    with open("app/config.json", "r") as f:
        data = json.load(f)
        fuel = data["FUEL_PRICE"]
        customer_list = [Customer(customer) for customer in data["customers"]]
        shop_list = [Shop(shop) for shop in data["shops"]]

        for customer in customer_list:
            print(f"{customer.name} has {customer.money} dollars")
            car = Car(customer.car)
            shop_to_choose = []

            for shop in shop_list:
                product_cost = shop.calculate_cost(customer.product_cart)
                distance = dist(customer.location, shop.location)
                trip_cost = car.trip_cost(distance, fuel) * 2
                total_cost = round(trip_cost + product_cost, 2)

                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {total_cost}")
                if customer.money > total_cost:
                    shop_to_choose.append((shop, total_cost))

            if not shop_to_choose:
                print(f"{customer.name} doesn't have enough money "
                      f"to make purchase in any shop")
                continue

            market, total_cost = sorted(shop_to_choose, key=lambda x: x[1])[0]
            print(f"{customer.name} rides to {market.name}\n")
            market.print_purchase_receipt(customer.name, customer.product_cart)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - total_cost} dollars\n")
