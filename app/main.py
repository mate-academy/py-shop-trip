import json
import datetime
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json") as file:
        date = json.load(file)
        fuel_price_date = date["FUEL_PRICE"]
        customers_date = date["customers"]
        shops_date = date["shops"]

    for customer in customers_date:
        name = customer["name"]
        customer_money = customer["money"]
        print(f"{name} has {customer_money} dollars")
        initial_location = customer["location"]
        fuel_consumption = customer["car"]["fuel_consumption"]
        product_cart = customer["product_cart"]
        car = Car(initial_location, fuel_price_date, fuel_consumption)
        min_expenses = float("inf")
        name_of_shop = ""

        for shop in shops_date:
            destination_location = shop["location"]
            product_shop = shop["products"]
            shop_name = shop["name"]

            date_of_shop = Shop(
                product_shop,
                product_cart,
                destination_location
            )
            money_for_all = date_of_shop.get_cheapest_shop(car)

            print(
                f"{name}'s trip to the {shop_name} costs {money_for_all}"
            )
            if (money_for_all < min_expenses
                    and customer_money > money_for_all):
                min_expenses = money_for_all
                name_of_shop = shop_name
                product = shop["products"]

        if not name_of_shop:
            print(
                f"{name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            print(f"{name} rides to {name_of_shop}\n")
            initial_location, destination_location \
                = destination_location, initial_location
            print("Date: "
                  + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                  )
            buy = Customer(name, customer["product_cart"], product)
            buy.buying_products()
            print(f"{name} rides home")
            change = customer["money"] - min_expenses
            print(f"{name} now has {change} dollars\n")
