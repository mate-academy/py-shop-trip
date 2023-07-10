import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
    customers = add_customers(config_data)
    shops = add_shops(config_data)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        roads_costs = dict()

        for shop in shops:
            x_distance = shop.location[0] - customer.location[0]
            y_distance = shop.location[1] - customer.location[1]
            distance = ((x_distance ** 2) + (y_distance ** 2)) ** (1 / 2)

            distance_cost = 2 * distance * customer.car.cost_per_km
            products_cost = sum(
                numbers * shop.products[product]
                for product, numbers in customer.products.items()
            )

            cost_trip = round(products_cost + distance_cost, 2)

            roads_costs[cost_trip] = shop

            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost_trip}"
            )

        if min(roads_costs.keys()) > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
        else:
            customer.money -= min(roads_costs)
            need_shop = roads_costs[min(roads_costs)]
            print(f"{customer.name} rides to {need_shop.name}\n"
                  f"\n{need_shop.print_check(customer)}\n"
                  f"\n{customer.name} rides home\n"
                  f"{customer.name} now has {customer.money} dollars\n"
                  )


def add_customers(config_data: dict) -> list[Customer]:
    customers_from_config = [
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
        for customer in config_data["customers"]
    ]

    return customers_from_config


def add_shops(config_data: dict) -> list[Shop]:

    shops_from_config = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in config_data["shops"]
    ]

    return shops_from_config
