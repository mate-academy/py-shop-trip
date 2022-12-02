import math
import datetime

from app.customers import Customers


def calculater(
        customer: Customers,
        shops: list,
        fuel_price: float
) -> None:
    print(f"{customer.name} has {customer.money} dollars")

    customer_location = customer.location
    fuel_consumption = customer.car["fuel_consumption"]
    total_value = 1_000_000
    best_shop = None
    product_price = 0

    for shop in shops:
        shop_location = shop.location

        distance = math.dist(customer_location, shop_location)
        price_ride = round(
            distance * fuel_price * 2 * (fuel_consumption / 100), 2
        )
        check_product = 0
        for product in customer.product_cart:
            check_product += \
                customer.product_cart[product] * shop.products[product]

        total_cost = round((check_product + price_ride), 2)
        print(f"{customer.name}'s trip to the {shop.name} costs {total_cost}")

        if total_cost < total_value:
            total_value = total_cost
            best_shop = shop
            product_price = check_product

    if total_value < customer.money:
        print(f"{customer.name} rides to {best_shop.name}\n")

        date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_time}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for product, amount in customer.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{amount * best_shop.products[product]} dollars")

        print(f"Total cost is {product_price} dollars")
        print("See you again!\n")

        print(f"{customer.name} rides home")
        customer.money -= total_value
        print(f"{customer.name} now has {customer.money} dollars\n")

    else:
        print(f"{customer.name} doesn't have enough money "
              f"to make purchase in any shop")
