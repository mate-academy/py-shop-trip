import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)
    fuel_price = data["FUEL_PRICE"]
    customers_data = data["customers"]
    shops_data = data["shops"]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"]),
        )
        for customer in customers_data
    ]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        )
        for shop in shops_data
    ]
    for customer in customers:
        customer_name = customer.name
        print(f"{customer_name} has {customer.money} dollars")

        trip_costs = {}
        for shop in shops:
            trip_cost = round(customer.get_trip_cost(shop, fuel_price), 2)
            trip_costs[shop] = trip_cost
            print(f"{customer_name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

        selected_shop: Shop = min(trip_costs, key=trip_costs.get)
        if trip_costs[selected_shop] > customer.money:
            print(f"{customer_name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        customer.ride(selected_shop)
        customer.money -= trip_costs[selected_shop]
        print(f"{customer_name} now has {customer.money} dollars\n")
