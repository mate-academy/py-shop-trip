import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_dict = json.load(file)
        customers = []
        shops = []
        for key, value in json_dict.items():
            if key == "FUEL_PRICE":
                fuel_price = value
            if key == "customers":
                customers_list = value
                for customer_json in customers_list:
                    car_dict = customer_json["car"]
                    car_obj = Car(
                        brand=car_dict["brand"],
                        fuel_consumption=car_dict["fuel_consumption"],
                    )
                    customer = Customer(
                        name=customer_json["name"],
                        product_cart=customer_json["product_cart"],
                        location=customer_json["location"],
                        money=customer_json["money"],
                        car=car_obj,
                    )
                    customers.append(customer)
            if key == "shops":
                shops_list = value
                for shop_json in shops_list:
                    shop = Shop(
                        name=shop_json["name"],
                        location=shop_json["location"],
                        products=shop_json["products"],
                    )
                    shops.append(shop)
    for customer in customers:
        count_price = customer.count_the_price(shops, fuel_price)
        customer.chose_the_shop(count_price)
