from math import sqrt


def distance_shop(shop_location, customer_location, fuel_consumption, cost_fuel):

    distance = count_distance(customer_location, shop_location)
    cost = cost_fuel * distance * fuel_consumption / 100
    two_way_cost = 2 * cost
    return two_way_cost


def count_distance(person: list, store: list):
    x1, y1 = person[0], person[1]
    x2, y2 = store[0], store[1]
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


