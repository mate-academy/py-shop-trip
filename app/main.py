import json

from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        info = json.load(file)

        fuel_price = info["FUEL_PRICE"]
        customers_data = info["customers"]
        shops_data = info["shops"]

    customers = []
    for customers_info in customers_data:
        car = Car(
            customers_info["car"]["brand"],
            customers_info["car"]["fuel_consumption"]
        )
        customer = Customer(
            customers_info["name"],
            customers_info["product_cart"],
            customers_info["location"],
            customers_info["money"],
            car
        )
        customers.append(customer)

    shops = []
    for shop_info in shops_data:
        shop = Shop(
            shop_info["name"],
            shop_info["location"],
            shop_info["products"]
        )
        shops.append(shop)

    for customer in customers:
        home_location = customer.location

        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:

            trip_cost = shop.calculate_trip_cost(
                customer,
                fuel_price
            )
            print(f"{customer.name}\'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")

            if trip_cost < min_trip_cost and trip_cost <= customer.money:
                min_trip_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            cheapest_shop.make_purchase(customer)
            customer.money -= min_trip_cost
            print(f"{customer.name} rides home")
            customer.location = home_location
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
