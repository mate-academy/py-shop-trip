import datetime
import sys
from app.utils import get_and_transform_data_from_json, calculate_distance


def shop_trip() -> None:
    try:
        fuel_price, customers, shops = get_and_transform_data_from_json()
        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            shop_and_price = []
            for shop in shops:
                current_trip_cost = round(calculate_distance(
                    customer.location,
                    shop.location,
                    fuel_price,
                    customer.car.fuel_consumption
                ) + sum(
                    customer.product_cart[key] * shop.products[key]
                    for key in customer.product_cart.keys()
                ), 2)
                shop_and_price.append((shop, current_trip_cost))
                print(f"{customer.name}'s"
                      f" trip to the {shop.name} costs"
                      f" {current_trip_cost}")
            cheapest_trip = min(shop_and_price, key=lambda tuple_: tuple_[1])
            if customer.money > cheapest_trip[1]:
                customer.money -= cheapest_trip[1]
                print(f"{customer.name} rides to {cheapest_trip[0].name}\n")
                date_time_now = datetime.datetime.now()
                date_to_print = date_time_now.strftime(
                    "Date: %d/%m/%Y %H:%M:%S"
                )
                print(f"{date_to_print}")
                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought: ")
                for product, price in customer.product_cart.items():
                    print(f"{price} {product}s"
                          f" for "
                          f"{price * cheapest_trip[0].products.get(product)}"
                          f" dollars")
                print(f"Total cost is"
                      f""" {sum(
                          customer.product_cart.get(key) *
                          cheapest_trip[0].products.get(key)
                          for key in customer.product_cart.keys())}"""
                      f" dollars")
                print("See you again!\n")
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has {customer.money} dollars\n")
            else:
                print(f"{customer.name}"
                      f" doesn't have enough money"
                      f" to make a purchase in any shop")
    except Exception as e:
        print(e)
        sys.exit()


shop_trip()
