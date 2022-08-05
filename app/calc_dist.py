def dist_from_customer(cus_x, cus_y, shop_x, shop_y):
    xx = cus_x - shop_x
    yy = cus_y - shop_y
    dist = (xx ** 2 + yy ** 2) ** 0.5
    return round(dist, 3)


def calculate_cost_of_ride(fuel_consumption, distance, fuel_price):
    return fuel_consumption * 0.01 * distance * fuel_price
