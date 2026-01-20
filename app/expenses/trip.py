import json

from app.classes.customer import Customer
from app.classes.shop import Shop


def distance_to_shop(customer: Customer, shop: Shop) -> float:
    return ((shop.location[0] - customer.location[0]) ** 2
            + (shop.location[1] - customer.location[1]) ** 2) ** 0.5


def find_shop_to_go(customer: Customer, shops: list) -> Shop:
    shop_to_go = None
    cost_of_the_trip = None
    for shop in shops:
        if cost_of_the_trip is None:
            cost_of_the_trip = trip_expanses(customer, shop)
            shop_to_go = shop
        elif trip_expanses(customer, shop) < cost_of_the_trip:
            cost_of_the_trip = trip_expanses(customer, shop)
            shop_to_go = shop
    return shop_to_go


def product_expenses(customer: Customer, shop: Shop) -> dict:
    product_costs = {
        "milk": customer.product_cart.milk * shop.products.milk,
        "bread": customer.product_cart.bread * shop.products.bread,
        "butter": customer.product_cart.butter * shop.products.butter
    }
    product_costs["total"] = (
        product_costs["milk"]
        + product_costs["bread"] + product_costs["butter"]
    )

    return product_costs


def trip_expanses(customer: Customer, shop: Shop) -> float:
    with open("app/config.json", "r") as file:
        date_from_file = json.load(file)
        product_costs = product_expenses(customer, shop)
        cost_of_the_trip = (
            distance_to_shop(customer, shop)
            * ((customer.car.fuel_consumption / 100)
               * date_from_file["FUEL_PRICE"])
        ) * 2
        cost_of_the_trip += product_costs["milk"]
        cost_of_the_trip += product_costs["bread"]
        cost_of_the_trip += product_costs["butter"]
    return round(cost_of_the_trip, 2)
