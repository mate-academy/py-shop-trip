import json
from datetime import datetime

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as f:
        config = json.load(f)
    customers = []
    for customer in config["customers"]:
        customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            )
        ))

    shops = []
    for shop in config["shops"]:
        shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        number = 10000
        for shop in shops:

            products_cost = 0
            for product in ("milk", "bread", "butter"):
                products_cost += (customer.product_cart[product]
                                  * shop.product_cart[product])
            shop_distance = shop.shop_distance(customer.location)
            trip_cost = customer.car.trip_cost(shop_distance,
                                               config["FUEL_PRICE"])
            trip_cost = round(products_cost + trip_cost, 2)

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

            if trip_cost < number:
                number = trip_cost
                shop_name = shop.name

        customer.money = round(customer.money - number, 2)
        if customer.money >= 0:
            print(f"{customer.name} rides to {shop_name}\n")
            print(f"Date: {datetime.now().strftime('%d/%m/%y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            products_cost = 0
            for shop in shops:
                if shop.name == shop_name:
                    for product in ("milk", "bread", "butter"):
                        product_cost = (shop.product_cart[product]
                                        * customer.product_cart[product])
                        print(f"{customer.product_cart[product]} "
                              f"milks for {product_cost} dollars")
                        products_cost += product_cost

            print(f"Total cost is {products_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")

        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
