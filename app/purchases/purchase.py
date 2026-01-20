import datetime
from typing import List

from app.customers.customer import Customer
from app.shops.shop import Shop


def _get_tripcost_to_shop(customer: Customer,
                          shop: Shop,
                          fuel_price: float):
    customer_x, customer_y = customer.location
    shop_x, shop_y = shop.location

    distance = ((shop_x - customer_x) ** 2 + (shop_y - customer_y) ** 2) ** 0.5
    fuel_price_per_km = customer.car["fuel_consumption"] / 100 * fuel_price
    tripcost = 2 * distance * fuel_price_per_km

    return round(tripcost, 2)


def _pick_cheapest_shop(customer, shops: List[Shop], fuel_price):
    prices = []

    for shop in shops:
        total_trip_price = _get_tripcost_to_shop(customer, shop, fuel_price)

        for product, amount in customer.product_cart.items():
            total_trip_price += (shop.products.get(product) * amount)

        if total_trip_price <= customer.money:
            prices.append((total_trip_price, shop))
        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {round(total_trip_price, 2)}")

    if not prices:
        print(f"{customer.name} doesn't have enough money to "
              "make purchase in any shop")
    else:
        cheapest_shop = min(prices)[1]
        customer.money -= round(min(prices)[0], 2)
        return cheapest_shop


def perform_purchase_of_products(customer, shops: List[Shop], fuel_price):
    print(f"{customer.name} has {customer.money} dollars")
    cheapest_shop = _pick_cheapest_shop(customer, shops, fuel_price)

    if cheapest_shop is not None:
        print(f"{customer.name} rides to {cheapest_shop.name}\n")

        _print_purchase_receipt(cheapest_shop, customer)

        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n")


def _print_purchase_receipt(shop: Shop, customer: Customer):
    total_products_cost = 0
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(f"Date: {now}\n"
          f"Thanks, {customer.name}, for you purchase!\n"
          "You have bought: ")

    for product, amount in customer.product_cart.items():
        product_cost = amount * shop.products.get(product)
        total_products_cost += product_cost
        products = product + "s" if amount > 1 else product
        print(f"{amount} {products} for {product_cost} dollars")

    print(f"Total cost is {total_products_cost} dollars\n"
          "See you again!\n")
