import json
import math
from datetime import datetime

from app.customer import Customer
from app.shop import Shop


def get_nearest_shop(customer: Customer, shop: Shop, FUEL_PRICE):
    distance = math.dist(customer.location, shop.location)
    cost_of_a_trip = (100 / customer.car.fuel_consumption) * FUEL_PRICE * distance
    return cost_of_a_trip



def get_cost_of_a_trip(FUEL_PRICE, distance: int | float, customer: Customer) -> int | float:
    return ((100 / customer.car.fuel_consumption) * FUEL_PRICE * distance) * 2


def get_the_cost_of_the_products_and_check(self, customer_name: str, product_cart: dict) -> int | float:
    total_price = 0
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(
        f"{today}\n"
        f"Thanks, {customer_name}, for you purchase!\n"
        f"You have bought:"
    )
    for name_of_product, number_of_products in product_cart.items():
        total_price += number_of_products * self.products[name_of_product]
        print(
            f"{number_of_products} {name_of_product} for "
            f"{number_of_products * self.products[name_of_product]} "
            f"dollars"
        )
    print(
        f"Total cost is {total_price} dollars\n"
        f"See you again!"
    )
    return total_price


def shop_trip() -> None:
    with open("config.json", "r") as file:
        data = json.load(file)

    FUEL_PRICE = data["FUEL_PRICE"]
    customers_list = [
        Customer.get_customer_info(customer) for customer in data["customers"]
    ]
    shops_list = [
        Shop.get_shop_info(shop) for shop in data["shops"]
    ]

    for customer in customers_list:
        for shop in shops_list:
            print(get_nearest_shop(customer, shop, FUEL_PRICE))


shop_trip()