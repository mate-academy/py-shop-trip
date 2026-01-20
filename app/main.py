import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop
from app.shopping_costs import count_trip_to_shop_value
from app.go_to_shop import go_to_shop


def shop_trip() -> None:
    with open("app/config.json", "r") as data:
        file_data = json.load(data)

    customers = create_customers(file_data["customers"])
    shops = create_shops(file_data["shops"])
    fuel_price = file_data["FUEL_PRICE"]

    shopping(customers, shops, fuel_price)


def create_customers(customers_data: list[dict]) -> list[Customer]:
    return [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
        ) for customer in customers_data
    ]


def create_shops(shops_data: list[dict]) -> list[Shop]:
    return [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ) for shop in shops_data
    ]


def shopping(
        customers: list[Customer],
        shops: list[Shop],
        fuel_price: float
) -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop, min_costs = count_trip_to_shop_value(
            customer=customer,
            shops=shops,
            fuel_price=fuel_price
        )

        if min_costs > customer.money:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make purchase in any shop"
            )
            continue

        go_to_shop(customer, cheapest_shop)

        money_rest = round(customer.money - min_costs, 2)

        print(f"{customer.name} now has {money_rest} dollars\n")
