import datetime
from app.car import Car
from app.customer import Customer
from app.shop import Shop
import json


def shop_trip() -> None:
    with open("config.json", "r") as config:
        infos = json.load(config)

    fuel_price = infos["FUEL_PRICE"]

    customers = []
    for data in infos["customers"]:
        car = Car(
            brand=data["car"]["brand"],
            fuel_consumption=data["car"]["fuel_consumption"]
        )

        customer = Customer(
            person_name=data["name"],
            product_cart=data["product_cart"],
            person_location=data["location"],
            money=data["money"],
            car=car
        )
        customers.append(customer)

    shops = []
    for data in infos["shops"]:
        shop = Shop(
            shop_name=data["name"],
            shop_location=data["location"],
            products=data["products"]
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.person_name} has {customer.money} dollars")

        best_shop = None
        best_cost = None
        home_location = customer.person_location

        for shop in shops:
            if not shop.can_sell(customer.product_cart):
                continue

            products_price = shop.products_cost(customer.product_cart)
            fuel_to_shop = customer.car.fuel_cost(
                home_location,
                shop.shop_location,
                fuel_price
            )

            fuel_to_home = customer.car.fuel_cost(
                shop.shop_location,
                home_location,
                fuel_price
            )

            total_cost = fuel_to_shop + fuel_to_home + products_price
            print(
                f"{customer.person_name}'s trip to the {shop.shop_name} "
                f"costs {total_cost:.2f}"
            )

            if best_cost is None or total_cost < best_cost:
                best_cost = total_cost
                best_shop = shop

        if best_cost is None or best_cost > customer.money:
            print(
                f"{customer.person_name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue
        print(f"{customer.person_name} rides to {best_shop.shop_name}")
        customer.person_location = best_shop.shop_location

        print()
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer.person_name}, for your purchase!")
        print("You have bought:")
        total_products_price = best_shop.products_cost(customer.product_cart)

        for product, quantity in customer.product_cart.items():
            price = round(best_shop.products[product] * quantity, 2)
            if price.is_integer():
                price = int(price)
            print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {total_products_price} dollars")
        print("See you again!\n")

        print(f"{customer.person_name} rides home")
        customer.person_location = home_location
        customer.money = customer.money - best_cost
        print(
            f"{customer.person_name} now has {customer.money:.2f} dollars\n"
        )
