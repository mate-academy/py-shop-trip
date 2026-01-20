from app.customers import Customer
from app.shops import Shop
from app.info import get_customers
from app.info import get_shops
from app.info import get_fuel_price


fuel_price = get_fuel_price()
shops = Shop.from_dict(get_shops())
customers = Customer.from_dict(get_customers())


def trip_cost() -> list:
    trip_prices = []
    for customer in customers:
        trip_prices_each_customer = []
        for shop in shops:
            shop_cart = 0
            x1 = customer.location[0]
            y1 = customer.location[1]
            x2 = shop.location[0]
            y2 = shop.location[1]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            for key in shop.products:
                shop_cart += customer.cart[key] * shop.products[key]
            fuel_rate = customer.car["fuel_consumption"]
            trip = shop_cart + 2 * distance * fuel_price * fuel_rate / 100
            trip_prices_each_customer.append(round(trip, 2))
        trip_prices.append(trip_prices_each_customer)
    return trip_prices
