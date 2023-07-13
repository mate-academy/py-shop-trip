import datetime

from .customer import make_list_of_instance, price_of_travel
from .shop import make_list_of_shop_instance, price_of_products, make_a_receipt


def shop_trip() -> None:
    customers_inst = make_list_of_instance()
    shop_inst = make_list_of_shop_instance()
    min_price = {}
    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    for customer in customers_inst:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shop_inst:
            price_of_product = price_of_products(customer.product_cart, shop.products)
            price_of_road = price_of_travel(customer.location, customer.car.fuel_consumption, shop.location)
            price_sum = price_of_product + price_of_road
            print(f"{customer.name}'s trip to the {shop.name} costs {price_sum}")
            min_price[shop.name] = price_sum
        min_pr_shop = min(min_price, key=min_price.get)
        if min(min_price.values()) <= customer.money:
            print(f"{customer.name} rides to {min_pr_shop}\n")
            make_a_receipt(
                customer.name,
                shop_inst,
                min_pr_shop,
                customer.product_cart,
                customer.location,
                date_time)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money - min(min_price.values())} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
