import math

from app.variables import Outskirts_Shop, Central_Shop, \
    Shop_24_7, fuel_price, customers


def outskirts_travel_cost():
    outskirts_total = {customer.name: 0 for customer in customers}
    for customer in customers:
        for item, amount in customer.product_cart.items():
            if item in Outskirts_Shop.products.keys():
                outskirts_total[customer.name] += \
                    amount * Outskirts_Shop.products[item]
        distance = \
            round(math.sqrt(
                (Outskirts_Shop.location[0] - customer.location[0])
                ** 2 + (Outskirts_Shop.location[1]
                        - customer.location[1]) ** 2), 2)
        outskirts_total[customer.name] += \
            round(((distance * customer.car["fuel_consumption"] / 100) *
                   fuel_price) * 2, 2)
    return outskirts_total


def central_travel_cost():
    central_total = {customer.name: 0 for customer in customers}
    for customer in customers:
        for item, amount in customer.product_cart.items():
            if item in Central_Shop.products.keys():
                central_total[customer.name] += \
                    amount * Central_Shop.products[item]
        distance = round(math.sqrt(
            (Central_Shop.location[0] - customer.location[0])
            ** 2 + (Central_Shop.location[1] - customer.location[1]) ** 2), 2)
        central_total[customer.name] += \
            round(((distance * customer.car
                    ["fuel_consumption"] / 100) * fuel_price) * 2, 2)
    return central_total


def shop_24_7_travel_cost():
    shop_24_7_total = {customer.name: 0 for customer in customers}
    for customer in customers:
        for item, amount in customer.product_cart.items():
            if item in Shop_24_7.products.keys():
                shop_24_7_total[customer.name] += amount * \
                    Shop_24_7.products[item]
        distance = round(math.sqrt((Shop_24_7.location[0] -
                                    customer.location[0])
                                   ** 2 + (Shop_24_7.location[1] -
                                           customer.location[1]) ** 2), 2)
        shop_24_7_total[customer.name] += \
            round(((distance * customer.car
                    ["fuel_consumption"] / 100) * fuel_price) * 2)
    return shop_24_7_total


def cheapest_trip():
    cheapest = {customer.name: ["", 0] for customer in customers}
    for customer in customers:
        if outskirts_travel_cost()[customer.name] < \
                central_travel_cost()[customer.name] and \
                outskirts_travel_cost()[customer.name] < \
                shop_24_7_travel_cost()[customer.name]:
            cheapest[customer.name] = ["Outskirts Shop",
                                       outskirts_travel_cost()[customer.name]]
            customer.product_price["milk"] = \
                customer.product_cart["milk"] * \
                Outskirts_Shop.products["milk"]
            customer.product_price["bread"] = \
                customer.product_cart["bread"] * \
                Outskirts_Shop.products["bread"]
            customer.product_price["butter"] = \
                customer.product_cart["butter"] * \
                Outskirts_Shop.products["butter"]
        elif central_travel_cost()[customer.name] < \
                outskirts_travel_cost()[customer.name] and \
                central_travel_cost()[customer.name] < \
                shop_24_7_travel_cost()[customer.name]:
            cheapest[customer.name] = ["Central shop",
                                       central_travel_cost()[customer.name]]
            customer.product_price["milk"] = \
                customer.product_cart["milk"] * \
                Central_Shop.products["milk"]
            customer.product_price["bread"] = \
                customer.product_cart["bread"] * \
                Central_Shop.products["bread"]
            customer.product_price["butter"] = \
                customer.product_cart["butter"] * \
                Central_Shop.products["butter"]
        elif shop_24_7_travel_cost()[customer.name] < \
                outskirts_travel_cost()[customer.name] and \
                shop_24_7_travel_cost()[customer.name] < \
                central_travel_cost()[customer.name]:
            cheapest[customer.name] = ["Shop '24/7'",
                                       shop_24_7_travel_cost()[customer.name]]
            customer.product_price["milk"] = \
                customer.product_cart["milk"] * Shop_24_7.products["milk"]
            customer.product_price["bread"] = \
                customer.product_cart["bread"] * Shop_24_7.products["bread"]
            customer.product_price["butter"] = \
                customer.product_cart["butter"] * Shop_24_7.products["butter"]

    return cheapest
