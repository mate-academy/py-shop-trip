import json
import math
from app.customer import Customer
from app.shop import Shop

with open("app/config.json") as source:
    info = json.load(source)


def trip_cost(fuel_price: float, costumer: Customer, shop: Shop) -> float:
    distance = math.dist(costumer.coords, shop.coords)
    total_fuel_cost = (costumer.fuel_cost(fuel_price) * distance) * 2
    total_price = 0

    for product in costumer.product_cart:
        total_price += costumer.product_cart[product] * shop.products[product]

    return round(total_fuel_cost + total_price, 2)


def counting_trips(person: Customer, shops: dict) -> dict:
    print(f"{person.name} has {person.money} dollars")
    result_trip = {}

    for trip in shops:
        cost = trip_cost(info["FUEL_PRICE"], person, shops[trip])
        print(
            f"{person.name}'s trip"
            f" to the {trip} costs {cost}"
        )
        result_trip[cost] = trip

    return result_trip


def counting_product_price(
        person: Customer,
        shops: dict,
        chosen_shop: Shop
) -> float:
    print(f"Thanks, {person.name}, for you purchase!")
    print("You have bought: ")
    result_price = 0

    for goods in person.product_cart:
        goods_price = (
            person.product_cart[goods]
            * shops[chosen_shop].products[goods]
        )
        result_price += goods_price
        print(
            f"{person.product_cart[goods]} {goods}s "
            f"for {goods_price} dollars"
        )

    print(f"Total cost is {result_price} dollars")
    print("See you again!")
    return result_price
