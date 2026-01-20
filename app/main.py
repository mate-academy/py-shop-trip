from app.customer import Customer
from app.shop import Shop
from app.car import Car
import json


def shop_trip() -> None:
    with open("app/config.json") as f:
        data = json.load(f)
        fuel_price = data["FUEL_PRICE"]
        customers_data = data["customers"]
        shops_data = data["shops"]

    customers = []
    for customer in customers_data:
        car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        new_customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            car
        )
        customers.append(new_customer)

    shops = []
    for shop in shops_data:
        new_shop = Shop(shop["name"], shop["location"], shop["products"])
        shops.append(new_shop)

    for customer in customers:
        cheapest_shop = None
        cheapest_cost = float("inf")

        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            trip_cost = shop.calculate_trip_cost(customer, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost:.2f}")

            if trip_cost < cheapest_cost and trip_cost <= customer.money:
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            cheapest_shop.make_purchase(customer)
            customer.return_home(cheapest_shop.location, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
