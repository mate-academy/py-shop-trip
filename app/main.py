from datetime import datetime
from app.customer import customers, cheapest_shop, Customer
from app.shop import shops, Shop


current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%m/%d/%Y %H:%M:%S")


def shop_trip():
    for customer in customers:
        print(f"{customer. name} has {customer.money} dollars")

        print(f"{customer.name} rides to {cheapest_shop(customer, shops) }")

        print(f"Date: {formatted_datetime}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
