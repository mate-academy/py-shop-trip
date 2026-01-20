import datetime
from math import dist

from app.customer import Customer
from app.shop import Shop


def trip(customer: Customer, shops: list[Shop], fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")

    min_price = float("inf")
    min_shop = None

    for shop in shops:
        distance = calculate_distance(customer, shop)
        distance_price = round(
            (distance / 100)
            * customer.car["fuel_consumption"]
            * fuel_price
            * 2
            , 2
        )
        product_price = 0

        for product, amount in customer.product_cart.items():
            cost = shop.products[product] * amount
            product_price += cost

        if distance_price + product_price < min_price:
            min_price = distance_price + product_price
            min_shop = shop

        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {distance_price + product_price}")

    if min_price > customer.money:
        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
        return

    print(f"{customer.name} rides to {min_shop.name}\n")

    buy_products(customer, min_shop)

    print(f"{customer.name} rides home")

    customer.money -= min_price
    print(f"{customer.name} now has {customer.money} dollars\n")


def buy_products(customer: Customer, shop: Shop) -> None:
    current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total_cost = 0

    print(f"Date: {current_date}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")

    for product, amount in customer.product_cart.items():
        cost = shop.products[product] * amount
        cost_str = str(cost).format(":.2f")
        print(f"{amount} {product}s for "
              f'{cost_str.strip(".0")} dollars')
        total_cost += cost

    print(f"Total cost is {total_cost} dollars")
    print("See you again!\n")


def calculate_distance(customer: Customer, shop: Shop) -> float:
    return dist(customer.location, shop.location)
