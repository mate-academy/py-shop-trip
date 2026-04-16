import datetime
import json

from app.shops import create_stores
from app.сustomers import create_customers
from app.calculate import Calculate


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        trip = json.load(config)
    if not trip["customers"] or not trip["shops"] or not trip["FUEL_PRICE"]:
        print("No correct data in json")
        return
    customers = create_customers(trip["customers"])
    shops = create_stores(trip["shops"])
    for name, customer in customers.items():
        calculator = Calculate(customer, shops)
        calculated_product_list = calculator.calculate_products(shops)
        calculated_road_list = calculator.calculate_road(shops,
                                                         trip["FUEL_PRICE"])
        total_price = calculator.total(calculated_product_list,
                                       calculated_road_list)
        best_shop = min(total_price, key=total_price.get)
        print(f"{name} has {customer.money} dollars")
        for shop_name, price in total_price.items():
            print(f"{name}'s trip to the {shop_name} costs {price}")
        if customer.money >= total_price[best_shop]:
            print(f"{customer.name} rides to {best_shop}\n")
            customer.ride_to_shop(shops[best_shop].location)
            date = datetime.datetime.now()
            print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {name}, for your purchase!")
            print("You have bought:")
            for product in calculated_product_list[best_shop]:
                best_price = calculated_product_list[best_shop][product]
                print(f"{customer.product_cart[product]} {product}s "
                      f"for {best_price:g} dollars")
            sum_products = sum(calculated_product_list[best_shop].values())
            print(f"Total cost is {sum_products} dollars")
            print("See you again!\n")
            customer.ride_home()
            print(f"{customer.name} rides home")
            customer.money -= total_price[best_shop]
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to "
                  "make a purchase in any shop")
