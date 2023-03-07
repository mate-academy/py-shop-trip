import json

from app.product import Product
from app.car import Car
from app.cart import Cart
from app.shop import Shop
from app.customer import Customer

with open("app/config.json", "r") as data_file:
    data_from_file = json.loads(data_file.read())

FUEL_PRICE = data_from_file.get("FUEL_PRICE")
customers = data_from_file.get("customers")
shops = data_from_file.get("shops")


def shop_trip() -> None:
    customers_list = []
    shops_list = []
    result = ""

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

    for customer_obj in customers_list:
        result += (customer_obj.print_report(shops_list)[:-2]
                   if customer_obj == customers_list[-1]
                   else customer_obj.print_report(shops_list))

    print(result)
