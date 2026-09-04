import json
import datetime

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]

    for customer in customers:
        customer_obj = Customer(customer)
        home_location = list(customer_obj.get_location())
        print(f"{customer_obj.name} has {customer_obj.money} dollars")
        car_obj = Car(customer["car"])

        min_shop_name = None
        min_shop_location = None
        min_total_cost = None
        min_products_cost = None

        for shop in shops:
            shop_ = Shop(shop)
            distance = shop_.calculate_distance(customer_obj.get_location())

            way_cost = car_obj.calculate_fuel_price(fuel_price, distance) * 2
            product_cart = customer_obj.get_product_cart()
            products_cost = shop_.calculate_products_cost(product_cart)

            sum_cost = products_cost[3]
            total_cost = round(way_cost + sum_cost, 2)

            if min_total_cost is None or total_cost < min_total_cost:
                min_total_cost = total_cost
                min_shop_name = shop_.name
                min_shop_location = shop_.location
                min_products_cost = products_cost

            print(f"{customer_obj.name}'s trip to the "
                  f"{shop_.name} costs {total_cost:.2f}")

        if customer_obj.can_afford(min_total_cost):
            print(f"{customer_obj.name} rides to {min_shop_name}")
            customer_obj.set_location(min_shop_location)
            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"\nDate: {date}")
            print(f"Thanks, {customer_obj.name}, for your purchase!\n"
                  f"You have bought:\n"
                  f"{customer_obj.product_cart['milk']} "
                  f"milks for {min_products_cost[0]} dollars\n"
                  f"{customer_obj.product_cart['bread']} "
                  f"breads for {min_products_cost[1]} dollars\n"
                  f"{customer_obj.product_cart['butter']} "
                  f"butters for {min_products_cost[2]} dollars\n"
                  f"Total cost is {min_products_cost[3]} dollars\n"
                  f"See you again!\n")

            customer_obj.set_location(home_location)
            res = round(customer_obj.money - min_total_cost, 2)
            print(f"{customer_obj.name} rides home\n"
                  f"{customer_obj.name} now has {res} dollars")
        else:
            print(f"{customer_obj.name} doesn't "
                  f"have enough money to make a purchase in any shop")
