import datetime

from app.json_data import create_elements, distance, shopping


def shop_trip():
    fuel_price, customers, shops = create_elements()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        distance_cost = {}
        receipt = ""
        for shop in shops:
            trip_price = round(
                distance(customer.location, shop.location)
                / 100 * customer.car.fuel_consumption * fuel_price,
                2
            ) * 2
            ttl_product_price, receipt = shopping(customer, shop)
            trip_price += ttl_product_price
            distance_cost[trip_price] = shop
            print(f"{customer.name}'s trip to the {shop.name} costs {trip_price}")
        min_shop_cost = min(distance_cost.keys())
        if min_shop_cost > customer.money:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
        else:
            the_best_shop = distance_cost[min_shop_cost]
            print(f"{customer.name} rides to {the_best_shop.name}")
            print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print(receipt)
            print("See you again!")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money - min_shop_cost} dollars")


shop_trip()
