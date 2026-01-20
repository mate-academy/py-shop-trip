import math
from datetime import datetime
from typing import Callable
from dataclasses import dataclass
from app.customer import Customer


@dataclass
class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict,
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.product_cost = None
        self.road_cost_one_way = None
        self.trip_cost = None


def make_shop_list(config: dict) -> list:
    shops = []
    for shop in config["shops"]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"],
            )
        )
    return shops


def calculate_products_cost(customer: Customer, shop : Shop) -> float:
    return round(
        sum(
            [
                count * shop.products[product]
                for product, count in customer.product_cart.items()
            ]
        ), 2
    )


def calculate_road_cost(customer: Customer,
                        shop: Shop, fuel_price: float) -> float:
    return round(
        math.dist(customer.location, shop.location) / 100
        * customer.car.fuel_consumption
        * fuel_price
        * 2,
        2
    )


def calculate_trip_to_the_shop(customer: Customer, shops: list[Shop],
                               fuel_price: float) -> Shop | None:

    cheapest_trip_cost = float("inf")
    cheapest_shop_to_go = None

    print(f"{customer.name} has {customer.money} dollars")

    for shop in shops:

        products_cost = calculate_products_cost(customer, shop)
        road_cost = calculate_road_cost(customer, shop, fuel_price)
        trip_cost = round(products_cost + road_cost, 2)

        print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")

        if trip_cost < customer.money and trip_cost <= cheapest_trip_cost:
            cheapest_shop_to_go = shop
            cheapest_trip_cost = trip_cost
            customer.road_cost_one_way = round(road_cost / 2, 2)
            customer.product_cost = products_cost
            customer.trip_cost = cheapest_trip_cost

    if cheapest_shop_to_go:

        print(f"{customer.name} rides to {cheapest_shop_to_go.name}\n")

        return cheapest_shop_to_go

    print(
        f"{customer.name} doesn't have enough money "
        f"to make a purchase in any shop"
    )
    return None


def add_info(func: Callable) -> Callable:
    def inner(customer: Customer, shop: Shop) -> None:
        current_date = datetime(2021, 1, 4, 12, 33, 41)
        current_date = current_date.strftime("%d/%m/%Y %X")
        # current_date = datetime.now().strftime("%d/%m/%Y %X")
        message = (
            f"Date: {current_date}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: "
        )
        print(message[:-1])
        func(customer, shop)
        print("See you again!\n")
    return inner


@add_info
def make_purchase(customer: Customer, shop: Shop) -> None:

    for product, count in customer.product_cart.items():
        price = count * shop.products[product]
        if isinstance(price, float) and price.is_integer():
            price = int(price)
        print(
            f"{count} {product}s for {price} dollars"
        )
    print(f"Total cost is {customer.product_cost} dollars")


def go_to_home(customer: Customer) -> None:
    customer.money -= customer.trip_cost
    print(
        f"{customer.name} rides home\n"
        f"{customer.name} now has {customer.money} dollars\n"
    )
