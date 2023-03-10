import datetime
import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def get_customers(customers: dict) -> list[Customer]:
    customers_list = []
    for customer in customers:
        car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        new_customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            car
        )
        customers_list.append(new_customer)
    return customers_list


def get_shops(shops: dict) -> list[Shop]:
    shops_list = []
    for shop in shops:
        new_shop = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        shops_list.append(new_shop)
    return shops_list


def buy_products(
        customer: Customer,
        chosen_shop: Shop,
        fuel_price: float
) -> None:
    current_date_time = datetime.datetime.now()
    time_now = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{customer.name} rides to {chosen_shop.name}\n")
    print(f"Date: {time_now}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought: ")

    total_cost = 0
    for product, quantity in customer.product_cart.items():
        products_cost = chosen_shop.products[product] * quantity
        if isinstance(products_cost, float):
            products_cost = round(products_cost, 1)

        print(f"{quantity} {product}s for {products_cost} dollars")
        total_cost += products_cost
    print(f"Total cost is {total_cost:.1f} dollars")
    print("See you again!")
    customer.money -= customer.road_to_shop(chosen_shop, fuel_price)
    print(f"\n{customer.name} rides home")

    print(f"{customer.name} now has {customer.money:.2f} dollars\n")


def visit_shop(
        customer: Customer,
        shops_list: list[Shop],
        fuel_price: float
) -> None:

    print(f"{customer.name} has {customer.money} dollars")
    is_enough_money = False
    for shop in shops_list:
        trip_cost = customer.road_to_shop(shop, fuel_price)
        print(f"{customer.name}'s trip to the {shop.name}"
              f" costs {trip_cost:.2f}")
        if trip_cost <= customer.money:
            is_enough_money = True
    if not is_enough_money:
        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
        return
    chosen_shop = customer.choose_shop(shops_list, fuel_price)
    buy_products(customer, chosen_shop, fuel_price)


def shop_trip() -> None:
    with open("app/config.json") as open_file:
        data = json.load(open_file)

    customers_list = get_customers(data["customers"])
    fuel_price = data["FUEL_PRICE"]

    shops_list = get_shops(data["shops"])

    for customer in customers_list:
        visit_shop(customer, shops_list, fuel_price)
