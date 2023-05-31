import math
import datetime
from typing import Union
from app.customer import Customer
from app.shop import Shop


def fuel_cost(customer: Customer, shop: Shop, fuel_price: float) -> float:
    fuel_consumption = float(customer.car["fuel_consumption"])
    cost_of_fuel = 0
    customer_location = customer.location
    shop_location = shop.location
    distance_to_shop = math.sqrt((shop_location[0]
                                  - customer_location[0])
                                 ** 2 + (shop_location[1]
                                         - customer_location[1]) ** 2)
    cost_of_fuel += (2 * distance_to_shop * (fuel_consumption / 100)
                     * float(fuel_price))

    cost_of_fuel = round(cost_of_fuel, 2)
    return cost_of_fuel


def cheapest_shop(customer: Customer,
                  shops: list[Shop],
                  fuel_price: float) -> Union[Shop, None]:
    total_cost = float("inf")
    selected_shop = None

    for shop in shops:
        cost = the_cost_of_shopping(customer, shop, fuel_price)
        print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        if cost < total_cost:
            total_cost = cost
            selected_shop = shop

    if total_cost > customer.money:
        print(f"{customer.name} doesn't have enough"
              f" money to make a purchase in any shop")
        return None
    else:
        customer.location = selected_shop.location
        print(f"{customer.name} rides to {selected_shop.name}")
        return selected_shop


def the_cost_of_shopping(customer: Customer,
                         shop: Shop,
                         fuel_price: float) -> float:
    cost = 0.0

    for product, quantity in customer.product_cart.items():
        price = float(shop.products[product])
        subtotal = price * quantity
        cost += subtotal

    cost += fuel_cost(customer, shop, fuel_price)

    cost = round(cost, 2)
    return cost


def calculate_total_cost(customer: Customer, shop: Shop) -> None:
    total_cost = 0
    output = (f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
              f"\nThanks,"
              f" {customer.name}, for your purchase!\nYou have bought: \n")

    for product, quantity in customer.product_cart.items():
        if product in shop.products:
            price = shop.products[product]
            cost = price * quantity
            total_cost += cost
            output += (f"{quantity} {product}s for"
                       f" {round(cost, 2)} dollars\n")

    total_cost = round(total_cost, 2)
    output += (f"Total cost is {round(total_cost, 2)}"
               f" dollars\nSee you again!")
    customer.location = customer.home_location
    print(output)


def cash_balance(customer: Customer,
                 shop: Shop,
                 fuel_price: float) -> None:
    cost_of_shopping = the_cost_of_shopping(customer, shop, fuel_price)
    customer_balance = float(customer.money) - float(cost_of_shopping)
    customer_balance = round(customer_balance, 2)
    print(f"\n{customer.name} rides home\n"
          f"{customer.name} now has "
          f"{round(customer_balance, 2)} dollars\n")
