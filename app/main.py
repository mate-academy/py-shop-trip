from app.car import Car
from app.shop import Shop
from app.customer import Customer
import json
import math
import datetime


def shop_trip():
    with open("config.json", "r") as read_file:
        config_data = json.load(read_file)
    car_list = []
    customer_list = []
    shop_list = []
    # create car object
    for customer_car in config_data["customers"]:
        car_list.append(Car(customer_car["car"]["brand"],
                            customer_car["car"]["fuel_consumption"]))
    for i, customer_info in enumerate(config_data["customers"]):
        customer_list.append(Customer(customer_info["name"],
                                      customer_info["product_cart"],
                                      customer_info["location"],
                                      customer_info["money"],
                                      car_list[i],))
    for shop_info in config_data["shops"]:
        shop_list.append(Shop(shop_info["name"],
                              shop_info["location"],
                              shop_info["products"],))

    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        cheap_shop = [float("inf"), 0, 0]
        for i, shop in enumerate(shop_list):
            distance = math.fabs(math.sqrt(math.pow(customer.location[0] - shop.location[0],2) +
                                           math.pow(customer.location[1] - shop.location[1],2)))
            price_road = (((distance * customer.car.fuel_consumption) / 100) * 2) * config_data["FUEL_PRICE"]
            product_sum = 0
            for product in shop.products:
                product_sum += shop.products[product] * customer.product_cart[product]
            all_sum = product_sum + price_road
            if all_sum < cheap_shop[0]:
                cheap_shop[0] = all_sum
                cheap_shop[1] = i
                cheap_shop[2] = product_sum
            print(f"{customer.name}'s trip to the {shop.name} costs {all_sum:.2f}")
        if customer.money < cheap_shop[0]:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {shop_list[cheap_shop[1]].name} \n")
            home_location =customer.location
            customer.location = shop_list[cheap_shop[1]].location
            print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print(f"You have bought:")
            for buy_product in customer.product_cart:
                print(f"{customer.product_cart[buy_product]} {buy_product}s for "
                      f"{customer.product_cart[buy_product] * shop_list[cheap_shop[1]].products[buy_product]} dollars")
            print(f"Total cost is {cheap_shop[2]} dollars")
            print(f"See you again!\n")
            print(f"{customer.name} rides home")
            customer.location = home_location
            customer.money = customer.money - cheap_shop[0]
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")




shop_trip()