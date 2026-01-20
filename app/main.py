import json
from math import dist
import datetime
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

        fuel_price = data["FUEL_PRICE"]
        customers = data["customers"]
        shops = data["shops"]

    for customer in customers:
        human = Customer(customer["name"],
                         customer["product_cart"],
                         customer["location"],
                         customer["money"],
                         Car(customer["car"]["brand"],
                             customer["car"]["fuel_consumption"]))

        print(f"{human.name} has {human.money} dollars")

        cheapest_shop = {
            "name": "",
            "price": 0,
            "products": {},
            "product_cost": 0
        }

        for shop in shops:
            store = Shop(shop["name"], shop["location"], shop["products"])

            distance = dist(human.location, store.location)

            fuel_needed = (distance * 2 * human.car.fuel_consumption) / 100
            fuel_cost = fuel_needed * fuel_price

            product_cost = 0

            for product_name, quantity in human.product_cart.items():
                if product_name in store.products:
                    product_cost += quantity * store.products[product_name]
                else:
                    pass

            total_price = round(fuel_cost + product_cost, 2)

            print(f"{human.name}'s trip to"
                  f" the {store.name} costs {total_price}")

            if cheapest_shop["name"] == "":
                cheapest_shop["price"] = total_price
                cheapest_shop["name"] = store.name
                cheapest_shop["products"] = store.products
                cheapest_shop["product_cost"] = round(product_cost, 1)
            elif cheapest_shop["price"] > total_price:
                cheapest_shop["price"] = total_price
                cheapest_shop["name"] = store.name
                cheapest_shop["products"] = store.products
                cheapest_shop["product_cost"] = round(product_cost, 1)

        if human.money >= cheapest_shop["price"]:
            print(f"{human.name} rides to {cheapest_shop['name']}")
            print()

            date = datetime.datetime.now()
            formatted_date = date.strftime("Date: %d/%m/%Y %H:%M:%S")

            print(formatted_date)

            print(f"Thanks, {human.name}, for your purchase!")
            print("You have bought:")

            for product_name, quantity in human.product_cart.items():
                price = 0.0

                if product_name in cheapest_shop["products"]:
                    price_in_shop = cheapest_shop["products"][product_name]
                    price += float(quantity * price_in_shop)

                if price.is_integer():
                    price = int(price)
                else:
                    price = round(price, 1)

                print(f"{quantity} {product_name}s for "
                      f"{price} dollars")

            print(f"Total cost is {cheapest_shop['product_cost']} dollars")
            print("See you again!")
            print()

            print(f"{human.name} rides home")
            print(f"{human.name} now has"
                  f" {human.money - cheapest_shop['price']} dollars")
            print()

        else:
            print(f"{human.name} doesn't have enough"
                  f" money to make a purchase in any shop")
