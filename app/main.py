from app.customer import Customer
from app.shop import Shop
from app.car import Car


from math import sqrt
import json
import datetime


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    check_data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    customers_list = [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"])
        for customer in data["customers"]
    ]

    shops_list = [
        Shop(shop["name"],
             shop["location"],
             shop["products"])
        for shop in data["shops"]
    ]

    cars_list = [
        Car(car["car"]["brand"], car["car"]["fuel_consumption"])
        for car in data["customers"]
    ]

    def product_cost(customer: Customer,
                     shop: Shop,
                     ) -> int | float:
        milk_cost = customer.product_cart["milk"] * shop.products["milk"]
        bread_cost = customer.product_cart["bread"] * shop.products["bread"]
        butter_cost = customer.product_cart["butter"] * shop.products["butter"]
        return milk_cost + bread_cost + butter_cost

    def cost_trip(customer: Customer,
                  car: Car,
                  shop: Shop
                  ) -> float | int:
        location = sqrt((shop.location[0] - customer.location[0]) ** 2
                        + (shop.location[1] - customer.location[1]) ** 2)
        cost_fuel = location * fuel_price * car.fuel_consumption / 100
        return round(cost_fuel * 2, 2)

    def go_to_home(remainder: int or float) -> str:
        return (f"{customer.name} rides home\n{customer.name}"
                f" now has {customer.money - remainder} dollars\n")

    for customer, car in zip(customers_list, cars_list):
        preferred_shop = [float("inf"), ""]
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_list:
            cost_trip_ = cost_trip(customer, car, shop)
            product_cost_ = product_cost(customer, shop)
            current_trip_cost = cost_trip_ + product_cost_
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {current_trip_cost}")

            if current_trip_cost < preferred_shop[0]:
                preferred_shop[0] = current_trip_cost
                preferred_shop[1] = shop.name

        if preferred_shop[0] <= customer.money:
            print(f"{customer.name} rides to {preferred_shop[1]}\n")
            for shop in shops_list:
                product_cart = customer.product_cart
                products = shop.products
                if str(shop.name) == preferred_shop[1]:
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
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")


if __name__ == "__main__":
    shop_trip()
