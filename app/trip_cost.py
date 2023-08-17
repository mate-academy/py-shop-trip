import json
from app.customer import customer_class
from app.shop import shop_class
from math import sqrt

fuel_cost_for_trip = []
with open(r"E:\projects\py-shop-trip\app\config.json", "r") as json_file:
    fuel_price = json.load(json_file)["FUEL_PRICE"]

for customer in customer_class:
    for shop in shop_class:
        distance = sqrt(
            abs((customer.location[0] - shop.location[0]) ** 2
                + (customer.location[1] - shop.location[1]) ** 2)
        )
        fuel = (customer.car["fuel_consumption"] * distance) / 100
        fuel_cost_for_trip.append(round(fuel * fuel_price * 2, 2))

purchases = []

for customer in customer_class:
    for shop in shop_class:
        milk = customer.product_cart["milk"] * shop.products["milk"]
        bread = customer.product_cart["bread"] * shop.products["bread"]
        butter = customer.product_cart["butter"] * shop.products["butter"]
        purchases.append(milk + bread + butter)

trip_cost = [purchases[index] + fuel_cost_for_trip[index]
             for index in range(len(purchases))]
