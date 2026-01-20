import json

from app.customer import Customer
from app.shop import Shop


def custumer_creation(customers: list) -> list:
    customers_instances = []
    for customer in customers:
        cus = Customer(**customer)
        customers_instances.append(cus)
    return customers_instances


def shop_creation(shops: list) -> list:
    shop_instances = [Shop(**shop) for shop in shops]
    return shop_instances


def final_assisment(
        customers_instances: list,
        shop_instances: list,
        fuel_price: int | float
) -> None:

    for customer in customers_instances:

        customer.money_start()

        shops_cost = {}
        for shop in shop_instances:
            products_cost = shop.products_cost(customer)
            fuel_cost = customer.car.fuel_cost(shop.distance(customer),
                                               fuel_price)
            trip_cost = round(products_cost + fuel_cost * 2, 2)

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

            shops_cost.update({trip_cost: shop})
            min_shop = shops_cost[min(shops_cost)]

        if customer.money >= min(shops_cost):
            min_shop.ride_to_shop(customer)
            min_shop.print_receipt(customer)
            customer.ride_to_home()
            customer.money -= min(shops_cost)
            customer.money_end()

        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


def shop_trip() -> None:

    with open("app/config.json", "r") as file:

        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customers = data["customers"]

    customers_instances = custumer_creation(customers)
    shop_instances = shop_creation(data["shops"])
    final_assisment(customers_instances, shop_instances, fuel_price)
