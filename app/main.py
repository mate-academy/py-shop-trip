from app.utils.utils import (
    file_handler,
    fuel_cost_one_way,
    trip_cost
)
from app.instances.customer import Customer
from app.instances.shop import Shop
from app.instances.car import Car


def shop_trip() -> None:
    config_data, fuel_price = file_handler("app/config.json")

    customers = []
    for customer in config_data["customers"]:
        customers.append(
            Customer
            (
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(customer["car"]["brand"],
                    customer["car"]["fuel_consumption"])
            )
        )

    shops = []
    for shop in config_data["shops"]:
        shops.append(
            Shop
            (
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trips_cost_by_shop = []

        for shop in shops:
            cost = trip_cost(customer, fuel_price, shop)
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            trips_cost_by_shop.append((shop, cost))

        shop, cost = min(trips_cost_by_shop, key=lambda x: x[1])

        if customer.money < cost:
            print(f"{customer.name} doesn't have enough money to make "
                  "a purchase in any shop")
            continue

        fuel_cost = fuel_cost_one_way(customer, fuel_price, shop)
        customer.ride_to_shop(fuel_cost, shop.name, shop.location)

        shop.serve_customer(customer)

        customer.ride_home(fuel_cost)
