import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json") as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]
    shops = [
        Shop(name=shop["name"],
             location=shop["location"],
             products=shop["products"]
             )
        for shop in config_data["shops"]
    ]
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"],
            ),
        )
        for customer in config_data["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs_of_trip = {}
        for shop in shops:
            total_cost = customer.calculate_total_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost}")
            costs_of_trip.update({total_cost: shop})
        lower_cost = min(costs_of_trip.keys())
        if lower_cost < customer.money:
            customer.ride_to_shop(costs_of_trip[lower_cost])
            customer.money -= lower_cost
            print(f"{customer.name} now has {customer.money} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
        if not customer.name == customers[-1].name:
            print("")
