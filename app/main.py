from app.shop import Shop
from app.customer import Customer
import datetime


def shop_trip() -> None:
    customer = Customer
    shop = Shop
    print(f"{customer.name} has {customer.money} dollars")
    print(f"{customer.name}'s trip to the"
          f" {shop.name} costs {shop.shopping_cost(customer)}")
    if (customer.money - shop.shopping_cost(customer)) < 0:
        print(f"{customer.name} doesn't"
              f" have enough money to make a purchase in any shop")
    else:
        print(f"{customer.name} rides to {shop.name}")
        print(f"Date: {datetime.datetime.now()}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        print(f"{customer.product_cart['milk']}"
              f" milks for {customer.product_cart['milk'] 
                            * shop.products['milk']} dollars")
        print(f"{customer.product_cart['bread']}"
              f" breads for {customer.product_cart['bread'] 
                             * shop.products['bread']} dollars")
        print(f"{customer.product_cart['butter']}"
              f" butters for {customer.product_cart['butter'] 
                              * shop.products['butter']} dollars")
        print(f"Total cost is"
              f" {shop.money_for_products(customer)} dollars")
        print("See you again!")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has"
              f" {customer.money - shop.shopping_cost(customer)} dollars")
