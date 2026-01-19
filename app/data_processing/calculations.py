from datetime import datetime
from math import sqrt, pow

from app.structures.coords import Coords
from app.structures.customer_profile import Car, Customer
from app.structures.shop import Shop


def calculating_distances(point1: Coords, point2: Coords) -> float:
    return sqrt(pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))


def ride_expenses(customer: Customer, shop: Shop) -> float:
    return (customer.car.fuel_consumption
            * calculating_distances(customer.location, shop.location)
            * Car.fuel_price / 100)


def groceries_cost(customer: Customer, shop: Shop) -> float:
    return sum([shop.products[item] * quantity
               for item, quantity in customer.product_cart.items()])


def shop_offer(customer: Customer, shop: Shop) -> tuple:
    trip_shop_home = ride_expenses(customer, shop) * 2
    cost = round((groceries_cost(customer, shop) + trip_shop_home), 2)
    return shop, cost


def attending_shop(customer: Customer, shop: Shop) -> None:
    date_of_shopping = datetime(2021, 1, 4, 12, 33, 41)
    date_of_shopping = date_of_shopping.strftime("%d/%m/%Y %H:%M:%S")
    customer.location = shop.location
    print(f"{customer.name} rides to {shop.name}")
    print()
    print(f"Date: {date_of_shopping}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    for item, quantity in customer.product_cart.items():
        price = quantity * shop.products[item]
        format_price = int(price) if price == int(price) else price
        format_item = item + ("s" if quantity > 1 else "")
        print(
            f"{quantity} {format_item} for {format_price} dollars"
        )
    print(f"Total cost is {groceries_cost(customer, shop)} dollars")
    print("See you again!")


def homecoming(customer: Customer, shop: Shop) -> None:
    customer.location = customer.home
    print(f"{customer.name} rides home")
    print(f"{customer.name} now has "
          f"{customer.money - shop_offer(customer, shop)[1]} dollars")
