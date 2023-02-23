import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def read_json() -> dict:
    with open("app/config.json", "r") as file_open:
        data = json.load(file_open)

    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]

    info_dict = {
        "customers": customers,
        "shops": shops,
        "fuel_price": fuel_price
    }

    return info_dict


def get_best_shop(info_dict: dict) -> None:

    for customer in info_dict["customers"]:
        car = Car(customer.car)

        print(f"{customer.name} has {customer.money} dollars")

        best_option_shop = {}

        for shop in info_dict["shops"]:
            distance = customer.get_distance(shop)
            cost = car.cost_of_travel(distance, info_dict["fuel_price"])
            total_cost = round(
                (shop.calculate_products_price(customer.product_cart)
                 + cost), 2
            )

            if total_cost <= customer.money:
                best_option_shop[total_cost] = shop

            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost}")

        if not best_option_shop:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make purchase in any shop"
            )
            break

        minimal_cost = min(cost for cost in best_option_shop)

        print(f"{customer.name} rides to "
              f"{best_option_shop[minimal_cost].name}\n")

        best_option_shop[minimal_cost].get_receipt(
            customer.name,
            customer.product_cart
        )
        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now "
            f"has {customer.money - minimal_cost} dollars\n"
        )


def shop_trip() -> None:
    info = read_json()
    get_best_shop(info)
