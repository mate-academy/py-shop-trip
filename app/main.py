import json
import math
from datetime import datetime

from app.customer import Customer
from app.shop import Shop


def get_the_cost_of_the_trip(
        customer: Customer,
        shop: Shop,
        fuel_price: int
) -> int | float:
    distance = math.dist(customer.location, shop.location) * 2
    cost_of_a_trip = round(
        (customer.car.fuel_consumption * fuel_price / 100) * distance, 2
    )
    return cost_of_a_trip


def get_the_cost_of_the_products(
        customer: Customer,
        shop: Shop
) -> int | float:
    cost_of_the_products = 0
    for name_of_product, number_of_products in customer.product_cart.items():
        cost_of_the_products += (
            number_of_products * shop.products[name_of_product]
        )
    return cost_of_the_products


def get_check(data: dict, customer: Customer, the_cheapest_store: str) -> None:
    the_cheapest_store_products = {}
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total_cost = 0

    for shop_name in data.get("shops"):
        if shop_name["name"] == the_cheapest_store:
            the_cheapest_store_products.update(shop_name.get("products"))

    print(
        f"{today}\n"
        f"Thanks, {customer.name}, for you purchase!\n"
        f"You have bought:"
    )

    for name, price in the_cheapest_store_products.items():
        total_cost += customer.product_cart[name] * price
        print(
            f"{customer.product_cart[name]} {name}s "
            f"for {customer.product_cart[name] * price} dollars"
        )
    print(
        f"Total cost is {total_cost} dollars\n"
        f"See you again!\n"
    )


def shop_trip() -> None:
    with open("config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers_list = [
        Customer.get_customer_info(customer) for customer in data["customers"]
    ]
    shops_list = [
        Shop.get_shop_info(shop) for shop in data["shops"]
    ]

    for customer in customers_list:
        print(
            f"{customer.name} has {customer.money} dollars"
        )
        the_cheapest_store = {}
        trips = []
        products = []

        for shop in shops_list:
            cost_of_the_trip = (
                get_the_cost_of_the_trip(customer, shop, fuel_price)
            )
            trips.append(cost_of_the_trip)
            cost_of_the_products = get_the_cost_of_the_products(customer, shop)
            products.append(cost_of_the_products)

            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{cost_of_the_trip + cost_of_the_products}"
            )

            if shop.name not in the_cheapest_store:
                the_cheapest_store[shop.name] = (
                    cost_of_the_trip + cost_of_the_products
                )

        the_cheapest_store = min(
            the_cheapest_store, key=the_cheapest_store.get
        )

        if customer.money > (cost_of_the_trip + cost_of_the_products):

            print(
                f"{customer.name} rides to "
                f"{the_cheapest_store}\n"
            )
            get_check(data, customer, the_cheapest_store)

            print(
                f"{customer.name} rides home\n"
                f"{customer.name} now has "
                f"{round(customer.money - min(trips) - min(products), 2)}"
                f" dollars\n"
            )

        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
