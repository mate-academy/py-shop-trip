import json

from app.shop import Shop
from app.car import Car
from app.product import Product
from app.customer import Customer
from app.cart import Cart


def shop_trip() -> None:
    customers_list = []
    shops_list = []
    result = ""

    with open("config.json") as file:
        data = json.loads(file.read())

    customers = data.get("customers")
    shops = data.get("shops")

    for customer in customers:
        customer_name = customer.get("name")
        customer_products_list = []
        customer_location = customer.get("location")
        customer_money = customer.get("money")
        customer_car = Car(customer.get("car").get("brand"),
                           customer.get("car").get("fuel_consumption"))

        for product, amount in customer.get("product_cart").items():
            customer_products_list.append(Cart(product, amount))

        customers_list.append(Customer(customer_name,
                                       customer_products_list,
                                       customer_location,
                                       customer_money,
                                       customer_car))

    for shop in shops:
        shop_name = shop.get("name")
        shop_location = shop.get("location")
        shop_products = []

        for product, price in shop.get("products").items():
            shop_products.append(Product(product, price))

        shops_list.append(Shop(shop_name, shop_location, shop_products))

    for customer in customers_list:
        if customer == customers_list[-1]:
            result += customer.print_message(shops_list)[:-2]
        else:
            result += customer.print_message(shops_list)

    print(result)
