from datetime import datetime
from app.customer import customers, cheapest_shop, Customer
from app.shop import shops, Shop


current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%m/%d/%Y %H:%M:%S")


def shop_trip():
    for customer in customers:

