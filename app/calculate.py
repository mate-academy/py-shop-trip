import datetime

from math import dist
from app.shop import Shop
from app.customer import Customer


def print_receipt(shop: Shop, customer: Customer) -> None:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {date}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought: ")
    total_cost = 0
    for product, count in customer.wanted_products.items():
        total_cost += count * shop.provided_products.get(product, 0)
        print(f"{count} {product if count < 2 else product + 's'} "
              f"for {count * shop.provided_products.get(product, 0)} dollars")
    print(f"Total cost is {round(total_cost, 2)} dollars")
    print("See you again!")


def choose_shop(customer: Customer,
                shops: list[Shop],
                fuel_price: float) -> int:
    result = []
    for shop in shops:
        trip_costs = calculate_cost_of_the_trip(customer, fuel_price, shop)
        result.append(trip_costs)
        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {trip_costs}")

    return shops[result.index(min(result))]


def calculate_cost_of_the_trip(customer: Customer,
                               fuel_price: float,
                               shop: Shop) -> float:
    distance = dist(customer.location, shop.location)
    logistic_expenses = round(
        (customer.car.fuel_consumption / 100) * (distance * 2) * fuel_price, 2)
    purchase_expenses = 0
    for product, quantity in customer.wanted_products.items():
        purchase_expenses += shop.provided_products.get(product, 0) * quantity
    return logistic_expenses + purchase_expenses


def go_to_shop(customer: Customer, shop: Shop, fuel_price: float) -> None:
    trip_price = calculate_cost_of_the_trip(customer, fuel_price, shop)
    customer.money -= trip_price
    print(f"{customer.name} rides to {shop.name}\n")
    print_receipt(shop, customer)
    print(f"\n{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars\n")


def can_afford_trip(customer: Customer,
                    shops: list[Shop],
                    fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    cheapest_shop = choose_shop(customer, shops, fuel_price)
    trip_cost = calculate_cost_of_the_trip(customer,
                                           fuel_price,
                                           cheapest_shop)
    if trip_cost < customer.money:
        go_to_shop(customer, cheapest_shop, fuel_price)
    else:
        print(f"{customer.name} "
              "doesn't have enough money to make a purchase in any shop")
