from math import dist
import datetime

from app.shop import Shop
from app.customer import Customer


def get_fuel_cost(
        customer: Customer,
        second_point: list[int]
) -> float:
    distance = dist(customer.location, second_point)
    customer.location = second_point
    fuel_cost = (customer.fuel_price * distance
                 * customer.car.fuel_consumption / 100)

    return fuel_cost


def get_product_cost(
        customer: Customer,
        shop: Shop,
) -> float:
    total_products_cost = 0
    products = customer.product_cart

    for product, number in products.items():
        products_cost = number * shop.product_cart[product]
        total_products_cost += products_cost

    return total_products_cost


def choose_shop(
        customer: Customer,
        shops: list[Shop]
) -> None:
    print(f"{customer.name} has {customer.money} dollars")

    trip_cost_list = [
        get_fuel_cost(customer, shop.location)
        + get_product_cost(customer, shop)
        + get_fuel_cost(customer, customer.home_location)
        for shop in shops
    ]

    for i in range(len(trip_cost_list)):
        print(
            f"{customer.name}'s trip to the {shops[i].name} "
            f"costs {round(trip_cost_list[i], 2)}"
        )

    if min(trip_cost_list) <= customer.money:
        index = trip_cost_list.index(min(trip_cost_list))
        customer.best_shop = shops[index]

        print(f"{customer.name} rides to {customer.best_shop.name}\n")
        get_receipt(customer, customer.best_shop)
        print(f"{customer.name} now has "
              f"{round(customer.money - trip_cost_list[index], 2)} "
              f"dollars\n")
    else:
        print(f"{customer.name} doesn't have enough "
              f"money to make a purchase in any shop")


def get_receipt(
        customer: Customer,
        shop: Shop
) -> None:
    formatted_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {formatted_date}\n"
          f"Thanks, {customer.name}, for your purchase!\n"
          f"You have bought:")

    for product, number in customer.product_cart.items():
        products_cost = round(number * shop.product_cart[product], 2)
        if products_cost % 1 == 0:
            products_cost = int(products_cost)
        print(f"{number} {product}s for {products_cost} dollars")

    total_product_cost = get_product_cost(customer, shop)
    print(f"Total cost is {round(total_product_cost, 2)} dollars\n"
          f"See you again!\n\n"
          f"{customer.name} rides home")
