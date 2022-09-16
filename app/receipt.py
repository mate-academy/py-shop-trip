import datetime

from decimal import Decimal
from math import sqrt


def print_receipt(customer, shops, fuel_price):
    print(f"{customer.name} has {customer.money} dollars")

    milk_amount = Decimal(str(customer.product_cart["milk"]))
    bread_amount = Decimal(str(customer.product_cart["bread"]))
    butter_amount = Decimal(str(customer.product_cart["butter"]))
    fuel_consumption = Decimal(str(customer.car["fuel_consumption"]))
    customer_location = customer.location

    shops_offer = {}
    payment = {}
    total_payment = {}

    for shop in shops:
        shop_location = shop.location
        milk_total = Decimal(str(shop.products["milk"])) * milk_amount
        bread_total = Decimal(str(shop.products["bread"])) * bread_amount
        butter_total = Decimal(str(shop.products["butter"])) * butter_amount
        products_total = milk_total + bread_total + butter_total

        x = (shop_location[0] - customer_location[0]) ** 2
        y = (shop_location[1] - customer_location[1]) ** 2
        distance_to_shop = Decimal(str(sqrt(x + y)))

        trip_cost = distance_to_shop * fuel_consumption\
            / Decimal("100") * Decimal(str(fuel_price)) * 2

        total_trip_price = round(trip_cost + products_total, 2)
        shops_offer[total_trip_price] = shop
        payment[shop.name] = products_total
        total_payment[shop.name] = total_trip_price
        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {total_trip_price}")

    min_shop_offer = shops_offer[min(shops_offer)]
    if customer.money < total_payment[min_shop_offer.name]:
        print(f"{customer.name} doesn't have enough money "
              f"to make purchase in any shop")
        return
    customer.money -= total_payment[min_shop_offer.name]
    print(f"{customer.name} rides to {min_shop_offer.name}" + "\n")
    print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(f"Thanks, {customer.name}, for you purchase!")
    print("You have bought: ")
    print(f"{milk_amount} milks for "
          f"{milk_amount * Decimal(str(min_shop_offer.products['milk']))} "
          "dollars"
          )
    print(f"{bread_amount} breads for "
          f"{bread_amount * Decimal(str(min_shop_offer.products['bread']))} "
          "dollars"
          )
    print(f"{butter_amount} butters for "
          f"{butter_amount * Decimal(str(min_shop_offer.products['butter']))} "
          "dollars"
          )
    print(f"Total cost is {payment[min_shop_offer.name]} dollars")
    print("See you again!" + "\n")
    print(f"{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars" + "\n")
