import json


from app.customer import Customer
from app.car import Car
from app.shop import Shop
import datetime


def shop_trip() -> None:
    with open("app/config.json") as json_file:
        all_data = json.load(json_file)
    # json_file = open("app/config.json")
    # all_data = json.load(json_file)

    customers = all_data.get("customers")
    shops = all_data.get("shops")
    fuel_price = all_data.get("FUEL_PRICE")

    customers_objects = []
    for customer in customers:
        car_dict = customer.get("car")
        new_car = Car(car_dict["brand"], car_dict["fuel_consumption"])
        new_customer = Customer(customer["name"],
                                customer["product_cart"], customer["location"],
                                customer["money"], new_car)
        customers_objects.append(new_customer)

    shops_objects = []
    for shop in shops:
        new_shop = Shop(shop["name"],
                        shop["location"],
                        shop["products"])
        shops_objects.append(new_shop)

    for customer in customers_objects:
        customer.show_yourself()
        command = ""
        best_price = 1000000.00
        best_shop = None
        home_location = customer.location[:]
        for shop in shops_objects:
            price = customer.trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {price}")
            if price < best_price:
                best_price = price
                best_shop = shop
                command = f"{customer.name} rides to {shop.name}"
        if customer.money < best_price:
            command = (f"{customer.name} doesn't have "
                       f"enough money to make a purchase in any shop")
        print(command)
        if customer.money >= best_price:
            customer.location = best_shop.location
            print("")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            best_shop.products_cost_with_command(customer.product_cart)
            print("See you again!")
            print("")
            print(f"{customer.name} rides home")
            actual_money = customer.money - best_price
            print(f"{customer.name} now has {actual_money:.2f} dollars")
            print("")
            customer.location = home_location[:]


if __name__ == "__main__":
    shop_trip()
