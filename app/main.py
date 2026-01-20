import json
import datetime

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        dictionary_file = json.load(file)

    fuel_price = dictionary_file["FUEL_PRICE"]

    customers = []
    for customer in dictionary_file["customers"]:
        car = Car(customer["car"]["brand"],
                  customer["car"]["fuel_consumption"])
        customer = Customer(customer["name"],
                            customer["product_cart"],
                            customer["location"],
                            customer["money"],
                            car)
        customers.append(customer)

    shops = []
    for shop in dictionary_file["shops"]:
        shop = Shop(shop["name"],
                    shop["location"],
                    shop["products"])
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = []
        for shop in shops:
            total_cost, fuel_cost = customer.calculate_trip_cost(shop,
                                                                 fuel_price)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {total_cost:.2f}")
            trip_costs.append((shop, total_cost, fuel_cost))

        best_shop, total_cost, fuel_cost = min(trip_costs, key=lambda x: x[1])

        if total_cost > customer.money:
            print(f"{customer.name} doesn't have enough money to make"
                  f" a purchase in any shop")
        else:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {formatted_time}")
            customer.buy_products(best_shop)
            customer.money -= fuel_cost
            print("")
            print(f"{customer.name} rides home")
            customer.location = customer.location
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
