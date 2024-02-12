import os
import json
from datetime import datetime
from app.customer import Customer
from app.shop import Shop
from app.car import Car
from app.utils import calculate_distance


def load_config() -> dict:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")
    with open(config_path, "r") as f:
        return json.load(f)


def format_money(amount: float) -> float:
    return f"{amount:.2f}".rstrip("0").rstrip(".")


def print_receipt(
        customer: "Customer",
        shop: "Shop" or None,
        total_cost: float,
        fixed_date: datetime) -> None:
    print(f"Date: {fixed_date.strftime('%m/%d/%Y %H:%M:%S')}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    for product, quantity in customer.product_cart.items():
        product_price = shop.products.get(product, 0)
        print(
            f"{quantity} {product}{'s' if quantity > 1 else ''}"
            f" for {format_money(quantity * product_price)} dollars")
    print(f"Total cost is {format_money(total_cost)} dollars")
    print("See you again!\n")


def shop_trip() -> None:
    config = load_config()
    fuel_price = config["FUEL_PRICE"]
    fixed_date = datetime(2021, 4, 1, 12, 33, 41)

    customers = [
        Customer(name=customer_data["name"],
                 product_cart=customer_data["product_cart"],
                 location=customer_data["location"],
                 money=customer_data["money"],
                 car=Car(customer_data["car"]["brand"],
                         customer_data["car"]["fuel_consumption"]))
        for customer_data in config["customers"]
    ]
    shops = [Shop(**data) for data in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {format_money(customer.money)} dollars")
        cheapest_shop = None
        min_total_cost = float("Infinity")

        for shop in shops:
            distance_to_shop = calculate_distance(
                customer.location, shop.location)
            trip_cost = customer.calculate_trip_cost(
                distance_to_shop, fuel_price)
            products_cost = shop.calculate_products_cost(
                customer.product_cart)
            total_cost = trip_cost + products_cost

            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {format_money(total_cost)}")

            if total_cost < min_total_cost\
                    and customer.has_enough_money(total_cost):
                cheapest_shop = shop
                min_total_cost = total_cost

        if cheapest_shop:
            distance_to_shop = calculate_distance(
                customer.location, cheapest_shop.location)
            trip_cost = customer.calculate_trip_cost(
                distance_to_shop, fuel_price)
            products_cost = cheapest_shop.calculate_products_cost(
                customer.product_cart)
            total_cost = trip_cost + products_cost

            customer.money -= total_cost
            customer.location = cheapest_shop.location
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            print_receipt(customer, cheapest_shop, products_cost, fixed_date)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f" {format_money(customer.money)} dollars\n")
        else:
            print(f"{customer.name}"
                  f" doesn't have enough money to make a purchase in any shop")
