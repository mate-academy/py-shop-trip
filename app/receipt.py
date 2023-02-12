import datetime
from decimal import Decimal
from math import sqrt


def print_receipt(customer, shops, fuel_price):
    print(f"{customer.name} has {customer.money} dollars")

    milk_amount = Decimal(str(customer.product_cart['milk']))
    bread_amount = Decimal(str(customer.product_cart['bread']))
    butter_amount = Decimal(str(customer.product_cart['butter']))
    customer_location = customer.location
    fuel_consumption = Decimal(str(customer.car['fuel_consumption']))

    shops_offers = {}
    payment = {}
    total_payment = {}
    for shop in shops:
        shop_location = shop.location
        milk_cost = Decimal(str(shop.products['milk'])) * milk_amount
        bread_cost = Decimal(str(shop.products['bread'])) * bread_amount
        butter_cost = Decimal(str(shop.products['butter'])) * butter_amount
        products_cost = milk_cost + bread_cost + butter_cost

        xs = (shop_location[0] - customer_location[0]) ** 2
        ys = (shop_location[1] - customer_location[1]) ** 2
        distance_from_shop = Decimal(str(sqrt(xs + ys)))

        numerator = distance_from_shop * fuel_consumption
        trip_price = numerator / Decimal('100') * Decimal(str(fuel_price)) * 2

        total_trip_price = round(trip_price + products_cost, 2)
        shops_offers[total_trip_price] = shop
        payment[shop.name] = products_cost
        total_payment[shop.name] = total_trip_price
        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {total_trip_price}")

    client_choice = shops_offers[min(shops_offers)]
    if customer.money < total_payment[client_choice.name]:
        print(f"{customer.name} doesn't have enough money to make "
              f"purchase in any shop")
        return
    customer.money -= total_payment[client_choice.name]
    print(f"{customer.name} rides to {client_choice.name}" + "\n")
    print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(f"Thanks, {customer.name}, for you purchase!")
    print("You have bought: ")
    print(f"{milk_amount} milks for "
          f"{milk_amount * Decimal(str(client_choice.products['milk']))} "
          "dollars"
          )
    print(f"{bread_amount} breads for "
          f"{bread_amount * Decimal(str(client_choice.products['bread']))} "
          "dollars"
          )
    print(f"{butter_amount} butters for "
          f"{butter_amount * Decimal(str(client_choice.products['butter']))} "
          "dollars"
          )
    print(f"Total cost is {payment[client_choice.name]} dollars")
    print("See you again!" + "\n")
    print(f"{customer.name} rides home")
    print(f"{customer.name} now has {customer.money} dollars" + "\n")
