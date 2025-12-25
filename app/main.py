import json
import datetime
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> str:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]
    customers_data = config_data["customers"]
    shops_data = config_data["shops"]

    customers = []
    shops = []

    for customer_data in customers_data:
        car_data = customer_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])

        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            car,
            customer_data["money"],
        )
        customers.append(customer)

    for shop_data in shops_data:
        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"],
            fuel_price
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {trip_cost}")
            if customer.calculate_money(shop):
                if trip_cost < cheapest_cost:
                    cheapest_cost = trip_cost
                    cheapest_shop = shop

        if cheapest_shop is not None:
            print(f"{customer.name} rides to "
                  f"{cheapest_shop.name}\n")
            current_time = datetime.datetime.\
                now().strftime("%d/%m/%Y %H:%M:%S")
            receipt = cheapest_shop.generate_receipt(
                customer, current_time, fuel_price)
            print(receipt)
            last_money = customer.money - cheapest_cost
            print(f"{customer.name} now has {last_money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
