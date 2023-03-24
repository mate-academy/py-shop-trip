import json
import math

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def get_dict_from_json() -> dict:
    with open("app/config.json", "r") as data:
        data = json.load(data)

    customers = []
    for customer in data["customers"]:
        customers.append(Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"], )
        ))

    shops = []
    for shop in data["shops"]:
        shops.append(Shop(
            name=shop["name"],
            products=shop["products"],
            location=shop["location"],
        ))
    return {
        "FUEL_PRICE": data["FUEL_PRICE"],
        "customers": customers,
        "shops": shops,
    }


def length_trip_calculation(x_point: list, y_point: list) -> float:
    return math.hypot(y_point[0] - x_point[0], y_point[1] - x_point[1])


def cost_trip_calculation(
        length_trip: float,
        fuel_consumption: float,
        fuel_price: float,
        cost_products: float,
) -> float:
    return round(
        length_trip * fuel_consumption / 100
        * fuel_price * 2 + cost_products, 2
    )


def shop_trip() -> None:
    data = get_dict_from_json()
    customers = data["customers"]
    shops = data["shops"]

    for customer in customers:
        # amount of money
        print(f"{customer.name} has "
              f"{customer.money} dollars")

        # path cost calculation
        for shop in shops:
            costs = {
                shop.name: cost_trip_calculation(
                    length_trip=length_trip_calculation(
                        shop.location, customer.location
                    ),
                    fuel_consumption=customer.car.fuel_consumption,
                    fuel_price=data["FUEL_PRICE"],
                    cost_products=(shop.products["milk"]
                                   * customer.product_cart["milk"]
                                   + shop.products["bread"]
                                   * customer.product_cart["bread"]
                                   + shop.products["butter"]
                                   * customer.product_cart["butter"]))
                for shop in shops
            }

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {costs[shop.name]}")
        shop_min_cost = "".join(
            ([k for k, v in costs.items() if v == min(costs.values())])
        )
        selected_shop = [
            shop for shop in shops if shop.name == shop_min_cost
        ][0]

        if min(costs.values()) <= customer.money:
            current_data = "04/01/2021 12:33:41"
            milk_price = \
                customer.product_cart["milk"] * \
                selected_shop.products["milk"]
            bread_price = \
                customer.product_cart["bread"] * \
                selected_shop.products["bread"]
            butter_price = \
                customer.product_cart["butter"] * \
                selected_shop.products["butter"]

            print(f"{customer.name} rides to {selected_shop.name}\n")
            print(f"Date: {current_data}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")
            print(
                f"{customer.product_cart['milk']} milks for "
                f"{milk_price} dollars")
            print(
                f"{customer.product_cart['bread']} breads for "
                f"{bread_price} dollars")
            print(
                f"{customer.product_cart['butter']} butters for "
                f"{butter_price} dollars")
            print(f"Total cost is "
                  f"{milk_price + bread_price + butter_price} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - min(costs.values())} dollars\n")
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
