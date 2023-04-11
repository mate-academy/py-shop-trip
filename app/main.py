import datetime
import json
import os.path
from typing import List

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def calculate_gasoline_cost(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> float:
    km = (
        round(
            (
                (customer.location[0] - shop.location[0]) ** 2
                + (customer.location[1] - shop.location[1]) ** 2
            )
            ** 0.5,
            2,
        )
        * 2
    )
    price = (customer.car.fuel_consumption / 100 * km) * fuel_price
    return price


def products_price(customer: Customer, shop: Shop) -> float:
    return sum(
        customer.product_cart[product] * shop.products[product]
        for product in customer.product_cart.keys()
    )


def print_date_purchased_items_and_their_cost(
        customer: Customer, shop: Shop
) -> None:
    print(
        f"Date: "
        f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        f"Thanks, {customer.name}, for your purchase!\n"
        f"You have bought: "
    )

    for product in customer.product_cart:
        print(
            f"{customer.product_cart[product]} {product}s for "
            f"{customer.product_cart[product] * shop.products[product]} "
            f"dollars"
        )
    print(
        f"Total cost is "
        f"{products_price(customer, shop)} dollars\n"
        f"See you again!\n"
    )


def print_cost_of_a_trip_to_all_stores_and_selected_store(
    customers_list: List[Customer], shop_list: List[Shop], fuel_price: float
) -> None:
    prices_dict = {}

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shop_list:
            trip_price = round(
                round(
                    calculate_gasoline_cost(customer, shop, fuel_price)
                    + products_price(customer, shop),
                    3,
                ),
                2,
            )

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_price}")
            prices_dict.update({shop.name: trip_price})

        min_price = min([index for index in prices_dict.values()])
        shop_name = list(prices_dict.keys())[
            list(prices_dict.values()).index(min_price)
        ]

        if min_price > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            print(f"{customer.name} rides to {shop_name}\n")

            shop_where_customer_go = [
                shop for shop in shop_list if shop.name == shop_name
            ][0]
            print_date_purchased_items_and_their_cost(
                customer, shop_where_customer_go
            )
            print_amount_of_money_left_after_purchases(
                customer, customer.money - min_price
            )


def print_amount_of_money_left_after_purchases(
    customer: Customer, money_in_account: float
) -> None:
    print(
        f"{customer.name} rides home\n"
        f"{customer.name} now has "
        f"{money_in_account} dollars\n"
    )


def shop_trip() -> None:
    path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "config.json"
    )

    with open(path, "r") as json_data:
        data = json.load(json_data)

    fuel_price = data["FUEL_PRICE"]
    customers_list = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"],
            ),
        )
        for customer in data["customers"]
    ]
    shop_list = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
        for shop in data["shops"]
    ]

    print_cost_of_a_trip_to_all_stores_and_selected_store(
        customers_list, shop_list, fuel_price
    )


if __name__ == "__main__":
    shop_trip()
