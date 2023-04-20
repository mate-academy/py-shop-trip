import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop
from app.calculate import products_cost
from app.calculate import trip_cost
from app.calculate import ride_shop
import datetime


def shop_trip() -> str:
    with open("app/config.json", "r") as f:
        data = json.load(f)
    shops = []
    for shop in data["shops"]:
        shop = Shop(name=shop["name"],
                    location=shop["location"],
                    products=shop["products"])
        shops.append(shop)
    for customer in data["customers"]:
        car = Car(brand=customer["car"]["brand"],
                  fuel_consumption=customer["car"]["fuel_consumption"])
        customer = Customer(name=customer["name"],
                            product_cart=customer["product_cart"],
                            location=customer["location"],
                            money=customer["money"],
                            car=car)

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            total_trip_cost = trip_cost(customer, shop)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {total_trip_cost}")

        choose_ride_shop = ride_shop(customer, shops)
        if customer.money < choose_ride_shop[1]:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {choose_ride_shop[0]}\n")

            date = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(f"Date: {date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")
            for shop in shops:
                if shop.name == choose_ride_shop[0]:
                    products = products_cost(customer, shop)
                    for product in customer.product_cart:
                        print(f"{customer.product_cart[product]} "
                              f"{product}s for {products[product]} dollars")
            print(f"Total cost is {sum(products.values())} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            new_customer_money = customer.money - choose_ride_shop[1]
            print(f"{customer.name} now has {new_customer_money} dollars\n")
