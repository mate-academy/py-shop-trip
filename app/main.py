import datetime
import json
import os


from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(os.path.join("app", "config.json"), "r") as config_file:
        json_content = json.load(config_file)
        fuel_price = json_content["FUEL_PRICE"]
        customers: list[Customer] = []
        shops: list[Shop] = []
        for customer_data in json_content["customers"]:
            customers.append(
                Customer(
                    customer_data["name"],
                    customer_data["product_cart"],
                    customer_data["location"],
                    customer_data["money"],
                    Car(
                        customer_data["car"]["brand"],
                        fuel_price,
                        customer_data["car"]["fuel_consumption"]
                    )
                )
            )
        for shop_data in json_content["shops"]:
            shops.append(Shop(*shop_data))
        for customer in customers:
            original_home_location = customer.location
            print(f"{customer.name} has {customer.money} dollars")
            shop_prices = {}
            for shop in shops:
                shop_prices[shop.name] = round(
                    customer.count_total_price(shop), 2
                )
                print(
                    f"{customer.name}'s trip to "
                    f"the {shop.name} costs {shop_prices[shop.name]}"
                )
            chosen_shop = min(shop_prices, key=shop_prices.get)
            if customer.money < min(shop_prices.values()):
                print(
                    f"{customer.name} doesn't have enough "
                    f"money to make a purchase in any shop"
                )
                continue
            shop_instance: Shop
            for shop in shops:
                if shop.name == chosen_shop:
                    shop_instance = shop
            print(f"{customer.name} rides to {chosen_shop}\n")
            customer.location = shop_instance.location  # pyright: ignore
            curr_date = datetime.datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            print(
                f"Date: {curr_date}"
                f"Thanks, {customer.name}, for your purchase!"
                "You have bought:"
            )
            product_price = 0.0
            for product, quantity in customer.product_cart.items():
                price = quantity * shop_instance.products[product]  # pyright: ignore # noqa: E501
                if price == int(price):
                    price = int(price)
                print(f"{quantity} {product}s for {price} dollars")
                product_price += price
            print(f"Total cost is {product_price} dollars")
            print(f"See you again!\n\n{customer.name} rides home")
            customer.location = original_home_location
            customer.money = customer.money - shop_prices[shop_instance.name]  # pyright: ignore # noqa: E501
            print(f"{customer.name} now has {customer.money} dollars\n")
