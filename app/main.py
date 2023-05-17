import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = add_customers()
    shops = add_shops()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        roads_costs = dict()

        for shop in shops:
            x_distance = shop.location[0] - customer.location[0]
            y_distance = shop.location[1] - customer.location[1]
            distance = ((x_distance ** 2) + (y_distance ** 2)) ** (1 / 2)

            distance_cost = 2 * distance * customer.car.cost_per_km()
            products_cost = 0

            for product, numbers in customer.products.items():
                products_cost += numbers * shop.products[product]

            cost_trip = round(products_cost + distance_cost, 2)

            roads_costs[cost_trip] = shop

            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost_trip}"
            )

        if min(roads_costs.keys()) > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
        else:
            customer.money -= min(roads_costs.keys())
            need_shop = roads_costs[min(roads_costs.keys())]
            print(f"{customer.name} rides to {need_shop.name}")
            print("\n" + need_shop.print_check(customer) + "\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")


def add_customers() -> list[Customer]:
    customers_from_config = list()

    with open("app/config.json", "r") as config:
        config_data = json.load(config)

        for customer in config_data["customers"]:
            customers_from_config.append(
                Customer(
                    name=customer["name"],
                    products=customer["product_cart"],
                    location=customer["location"],
                    money=customer["money"],
                    car=Car(
                        brand=customer["car"]["brand"],
                        fuel_consumption=customer["car"]["fuel_consumption"],
                        fuel_price=config_data["FUEL_PRICE"]
                    )
                )
            )

    return customers_from_config


def add_shops() -> list[Shop]:
    shops_from_config = list()

    with open("app/config.json", "r") as config:
        config_data = json.load(config)

        for shop in config_data["shops"]:
            shops_from_config.append(
                Shop(
                    name=shop["name"],
                    location=shop["location"],
                    products=shop["products"]
                )
            )

    return shops_from_config
