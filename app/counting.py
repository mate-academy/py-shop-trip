import datetime
import math


def counting(customer, shops, fuel_price):
    print(f"{customer.name} has {customer.money} dollars")

    customer_location = customer.location
    fuel_consumption = customer.car["fuel_consumption"]

    total_value = 1_000_000
    best_shop = None
    total_cost_products = 0

    for shop in shops:
        shop_location = shop.location

        distance = math.dist(customer_location, shop_location)
        cost_ride = \
            round(2 * distance * fuel_price * (fuel_consumption / 100), 2)

        product_cost = 0
        for product in customer.product_cart:
            product_cost += \
                customer.product_cart[product] * shop.products[product]

        total_cost = round((cost_ride + product_cost), 2)
        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {total_cost}")

        if total_cost < total_value:
            total_value = total_cost
            best_shop = shop
            total_cost_products = product_cost

    if total_value < customer.money:
        print(f"{customer.name} rides to {best_shop.name}" + "\n")

        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {current_date}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for product, amount in customer.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{amount * best_shop.products[product]} dollars")

        print(f"Total cost is {total_cost_products} dollars\n"
              f"See you again!\n")
        print(f"{customer.name} rides home")
        customer.money -= total_value
        print(f"{customer.name} now has {customer.money} dollars" + "\n")
    else:
        print(f"{customer.name} doesn't have enough "
              f"money to make purchase in any shop")
