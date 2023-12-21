import json

from app.shop import Shop
from app.customer import Customer


def shop_trip():

    with open("D:/Python_projects/User/py-shop-trip/app/config.json", "r") as file:
        data = json.load(file)

    customers_list = [Customer(customer) for customer in data["customers"]]
    shops_list = [Shop(shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]

    for customer in customers_list:

        chosen_shop = customer.chose_shop(shops_list, fuel_price)
        if chosen_shop:
            customer.driving_home()


if __name__ == "__main__":
    shop_trip()
