import json

from app.shop import Shop
from app.car import Car
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as data_file:
        data = json.load(data_file)

    fuel_price = data["FUEL_PRICE"]
    customers_data = data["customers"]
    shops_data = data["shops"]

    shops = {}
    for shop_data in shops_data:
        shop_name = shop_data["name"]
        shop_location = shop_data["location"]
        products = shop_data["products"]

        shop = Shop(shop_name, shop_location, products)
        shops[shop_name] = shop

    for customer_data in customers_data:
        customer_car = Car(
            customer_data["car"]["brand"],
            customer_data["car"]["fuel_consumption"]
        )
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            customer_car
        )

        min_total_cost = float("inf")
        best_shop = None

        customer.initial_money()
        for shop_name, shop in shops.items():
            total_cost = (
                customer.distance(
                    shop.shop_location,
                    customer_car.fuel_consumption,
                    fuel_price
                )
            )

            for product_name, price in customer.product_cart.items():
                cost = price * shop.products[product_name]
                total_cost += cost

            print(f"{customer.name}'s trip to the "
                  f"{shop_name} costs {round(total_cost, 2)}")

            if total_cost < min_total_cost and total_cost <= customer.money:
                min_total_cost = total_cost
                best_shop = shop

        if best_shop is not None:
            print(f"{customer.name} rides to {best_shop.shop_name}\n")

            customer.time_for_shopping(best_shop)
            customer.money -= min_total_cost
            print(f"{customer.name} rides home")
            print(f"{customer.name} "
                  f"now has {round(customer.money, 2)} dollars\n")

        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
