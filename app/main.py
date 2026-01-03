import json

from app.customer import Customer
from app.shop import get_shop_list
from app.car import Car


def get_customer_list(data: dict) -> list[Customer]:
    customers_list = data.get("customers")
    fuel_price = data.get("FUEL_PRICE")

    return [
        Customer(
            name=person.get("name"),
            product_cart=person.get("product_cart"),
            location=person.get("location"),
            money=person.get("money"),
            car=Car(
                person["car"].get("brand"),
                person["car"].get("fuel_consumption"),
                fuel_price
            )
        )
        for person in customers_list
    ]


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    customers = get_customer_list(data)
    shops = get_shop_list(data)

    for customer in customers:
        min_cost = 1000000
        cheapest_shop = None
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            customer.get_shop(shop, customer.car)

            if customer.cost_of_trip(shop, customer.car) < min_cost:
                min_cost = customer.cost_of_trip(shop, customer.car)
                cheapest_shop = shop
        if min_cost < customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.print_receipt(cheapest_shop)
            print(f"{customer.name} rides home")
            cost = customer.cost_of_trip(cheapest_shop, customer.car)
            print(f"{customer.name} now has {customer.money - cost} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


# shop_trip()
