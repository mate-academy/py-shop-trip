import json

from app.Shop import Shop
from app.Car import Car
from app.Customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers_data = data["customers"]
    shops_data = data["shops"]

    shops = []
    for shop_info in shops_data:
        shop_name = shop_info["name"]
        shop_location = shop_info["location"]
        products = shop_info["products"]
        shop = Shop(shop_name, shop_location, products)
        shops.append(shop)

    for customer_data in customers_data:
        customer_car = Car(
            customer_data["car"]["brand"],
            customer_data["car"]["fuel_consumption"])
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            customer_car)

        min_cost = float("inf")
        cheapest_shop = None

        customer.customer_money()
        for shop in shops:
            total_cost = customer.distance(
                shop.shop_location, customer_car.fuel_consumption, fuel_price)
            total_cost += sum(
                price * shop.products[product_name]
                for product_name, price in customer.product_cart.items())
            print(f"{customer.name}'s trip to the "
                  f"{shop.shop_name} costs {round(total_cost, 2)}")

            if total_cost < min_cost and total_cost <= customer.money:
                min_cost = total_cost
                cheapest_shop = shop

        if cheapest_shop is not None:
            print(f"{customer.name} rides to {cheapest_shop.shop_name}\n")
            customer.shopping(cheapest_shop)
            customer.money -= min_cost
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(
                f"{customer.name} "
                f"doesn't have enough money to make a purchase in any shop"
            )
