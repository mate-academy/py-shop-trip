import os
import json
import datetime
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as json_file:
        data = json.load(json_file)

    fuel_price = data["FUEL_PRICE"]
    shops = []
    customers = []

    for shop in data["shops"]:
        shops.append(
            Shop(shop["name"], shop["location"], shop["products"])
        )

    for customer in data["customers"]:
        car_customer = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )

        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                car_customer,
            )
        )

    for customer in customers:
        print(f"{customer.name} has {round(customer.money, 2)} dollars")

        customer_location = customer.location
        shop_prices = {}

        for shop in shops:
            total_cost = round(
                customer.total_cost_calculation(fuel_price, shop), 2
            )

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")
            shop_prices[shop] = total_cost

        min_price_shop = min(shop_prices, key=lambda x: shop_prices[x])
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")

        if shop_prices[min_price_shop] <= customer.money:
            print(f"{customer.name} rides to {min_price_shop.name}\n")

            customer.location = min_price_shop.location

            print(f"Date: {now}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer.product_cart.items():
                price = round(quantity * min_price_shop.products[product], 2)

                print(f"{quantity} {product}s for "
                      f"{price} dollars")

            print(f"Total cost is "
                  f"{min_price_shop.cart_cost_calculation(
                      customer.product_cart)} dollars")

            print("See you again!\n")

            print(f"{customer.name} rides home")
            customer.location = customer_location
            customer.money -= shop_prices[min_price_shop]
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
