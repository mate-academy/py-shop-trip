import json
from app.customer import Customer, Car
from app.shop import Shop
from os import path


def load_data(file_name: str) -> tuple:
    with open(file_name, "r") as file_in:
        data = json.load(file_in)
    customers = create_customers(data["customers"])
    shops = create_shops(data["shops"])
    fuel_price = data["FUEL_PRICE"]
    return fuel_price, customers, shops


def create_customers(data: dict) -> list[Customer]:
    return [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(**customer["car"]),
        )
        for customer in data
    ]


def create_shops(data: dict) -> list[Shop]:
    return [Shop(**shop) for shop in data]


def shop_trip() -> None:
    file_path = path.join("app", "config.json")
    fuel_price, customers, shops = load_data(file_path)

    for customer in customers:
        best_shop = None
        min_cost = float("inf")
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            distance = shop.calculate_distance(customer)
            trip_cost = customer.car.calculate_trip(fuel_price, distance)
            products_cost = sum(
                shop.products.get(item, 0) * value
                for item, value in customer.product_cart.items()
            )
            total_cost = trip_cost + products_cost
            print(
                f"{customer.name}'s trip "
                f"to the {shop.name} costs {total_cost}"
            )

            if total_cost < min_cost:
                best_shop = shop
                min_cost = total_cost
        if min_cost > customer.money:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make a purchase in any shop"
            )
            continue
        print(f"{customer.name} rides to {best_shop.name}")
        best_shop.print_receipt(customer)
        customer.return_home(customer.money - min_cost)
