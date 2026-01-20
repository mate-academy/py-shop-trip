from datetime import datetime
from math import dist
from app.customer import Customer
from app.shop import Shop

current_date = datetime(
    2021, 1, 4, 12, 33, 41
).strftime("%d/%m/%Y %H:%M:%S")


def calculate_trip_cost(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> float:
    distance = dist(customer.location, shop.location)
    fuel_consumption = customer.car.fuel_consumption
    distance_price = (distance / 100) * fuel_consumption * fuel_price * 2
    product_price = sum(
        shop.products[product] * amount
        for product, amount in customer.product_cart.items()
    )
    total_price = distance_price + product_price
    return total_price


def find_best_shop(
        customer: Customer,
        shops: list[Shop],
        fuel_price: float
) -> tuple[Shop, float]:
    min_price = float("inf")
    min_shop = None
    for shop in shops:
        total_price = calculate_trip_cost(customer, shop, fuel_price)
        if total_price < min_price:
            min_price = total_price
            min_shop = shop
        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {round(total_price, 2)}")
    return min_shop, min_price


def print_purchase_details(
        customer: Customer,
        shop: Shop
) -> None:
    print(f"Date: {current_date}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    total_cost = 0
    for product, amount in customer.product_cart.items():
        cost = shop.products[product] * amount
        if cost != int(cost):
            cost_str = str(round(cost, 2))
        else:
            cost_str = str(int(cost))
        print(f"{amount} {product}s for {cost_str} dollars")
        total_cost += cost
    print(f"Total cost is {total_cost} dollars")
    print("See you again!\n")


def trip(
        customer: Customer,
        shops: list[Shop],
        fuel_price: float
) -> None:
    print(f"{customer.name} has {customer.money} dollars")

    min_shop, min_price = find_best_shop(customer, shops, fuel_price)

    if min_price > customer.money:
        print(f"{customer.name} doesn't have enough money to make a purchase "
              f"in any shop")
        return

    print(f"{customer.name} rides to {min_shop.name}\n")
    print_purchase_details(customer, min_shop)

    print(f"{customer.name} rides home")
    customer.money -= min_price
    print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
