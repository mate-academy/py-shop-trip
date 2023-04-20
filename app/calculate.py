import operator
from app.customer import Customer
from app.shop import Shop
from math import sqrt


def fuel_cost(customer: Customer, shop: Shop) -> float:
    fuel_price = 2.4
    distance = sqrt(((customer.location[0] - shop.location[0])**2)
                    + ((customer.location[1] - shop.location[1])**2))
    shop_trip_cost = round((customer.car.fuel_consumption / 100)
                           * (distance * 2) * fuel_price, 2)
    return shop_trip_cost


def products_cost(customer: Customer, shop: Shop) -> dict:
    shop_products_cost = {}
    for product, price in customer.product_cart.items():
        shop_products_cost[product] = (customer.product_cart[product]
                                       * shop.products[product])
    return shop_products_cost


def trip_cost(customer: Customer, shop: Shop) -> float:
    shop_trip_cost = fuel_cost(customer, shop)
    shop_products_cost = products_cost(customer, shop)
    total_trip_price = shop_trip_cost + sum(shop_products_cost.values())
    return total_trip_price


def ride_shop(customer: Customer, shops: list) -> dict:
    trip_cost_dict = {}
    for shop in shops:
        total_trip_price = trip_cost(customer, shop)
        trip_cost_dict[shop.name] = total_trip_price
    choose_shop = min(trip_cost_dict.items(), key=operator.itemgetter(1))
    return choose_shop
