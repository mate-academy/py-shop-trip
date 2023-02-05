from math import sqrt
import json
import datetime

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    check_data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    customer_list = [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"])
        for customer in data["customers"]
    ]

    shop_list = [
        Shop(shop["name"],
             shop["location"],
             shop["products"])
        for shop in data["shops"]
    ]

    car_list = [
        Car(car["car"]["brand"], car["car"]["fuel_consumption"])
        for car in data["customers"]
    ]

    def go_to_home(remainder: int | float) -> str:
        return (f"{customer.name} rides home\n{customer.name}"
                f" now has {customer.money - remainder} dollars\n")

    def purchase_product() -> None:
        products = shop.products
        product_cart = customer.product_cart
        print(f"{customer.name} rides to {preferred_shop[1]}\n")
        print(f"Date: {check_data}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        print(f"{product_cart['milk']} milks for "
              f"{products['milk'] * product_cart['milk']} "
              "dollars")
        print(f"{product_cart['bread']} breads for "
              f"{products['bread'] * product_cart['bread']}"
              " dollars")
        print(f"{product_cart['butter']} butters for "
              f"{products['butter'] * product_cart['butter']} "
              "dollars")
        total_cost = sum([value * shop.products[key]
                          for key, value in product_cart.items()])
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(go_to_home(preferred_shop[0]))

    for customer, car in zip(customer_list, car_list):
        preferred_shop = [float("inf"), ""]
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shop_list:
            cost_trip_ = shop.cost_trip(car, customer, fuel_price)
            product_cost_ = shop.product_cost(customer)
            current_trip_cost = cost_trip_ + product_cost_
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {current_trip_cost}")

            if current_trip_cost < preferred_shop[0]:
                preferred_shop[0] = current_trip_cost
                preferred_shop[1] = shop.name

        if preferred_shop[0] <= customer.money:

            for shop in shop_list:
                if str(shop.name) == preferred_shop[1]:
                    purchase_product()
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")


if __name__ == "__main__":
    shop_trip()
