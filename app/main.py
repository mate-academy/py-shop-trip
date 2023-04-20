import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop
from app.calculate import products_cost
from app.calculate import trip_cost
from app.calculate import ride_shop
import datetime


def shop_trip() -> None:
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
                  fuel_consumption=customer["car"]["fuel_consumption"],
                  fuel_price=data["FUEL_PRICE"])
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

        ride_shop_name = ride_shop(customer, shops)
        for shop in shops:
            if shop.name == ride_shop_name:
                ride_shop_cost = trip_cost(customer, shop)
                if customer.money < ride_shop_cost:
                    print(f"{customer.name} doesn't have "
                          f"enough money to make a purchase in any shop")
                else:
                    print(f"{customer.name} rides to {ride_shop_name}\n")
                    date = (datetime.datetime.now().
                            strftime("%d/%m/20%y %H:%M:%S"))
                    print(f"Date: {date}")
                    print(f"Thanks, {customer.name}, for your purchase!")
                    print("You have bought: ")
                    for shop in shops:
                        if shop.name == ride_shop_name:
                            products = products_cost(customer, shop)
                            for product in customer.product_cart:
                                print(f"{customer.product_cart[product]} "
                                      f"{product}s for "
                                      f"{products[product]} dollars")
                    print(f"Total cost is {sum(products.values())} dollars")
                    print("See you again!\n")
                    print(f"{customer.name} rides home")
                    new_customer_money = customer.money - ride_shop_cost
                    print(f"{customer.name} now has"
                          f" {new_customer_money} dollars\n")
