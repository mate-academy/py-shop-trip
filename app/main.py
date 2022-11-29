import json
import datetime

from app.car import Car
from app.customer import Customer
from app.shops import Shop

FUEL_PRICE = 0


def init_all_inst() -> tuple:
    global FUEL_PRICE

    with open("app/config.json", "r") as file:
        data_dict = json.load(file)

    customers = []
    shops = []
    FUEL_PRICE = float(data_dict["FUEL_PRICE"])

    for _customer in data_dict["customers"]:
        _car = Car(
            brand=_customer["car"]["brand"],
            fuel_consumption=_customer["car"]["fuel_consumption"])

        customers.append(Customer(
            name=_customer["name"],
            location=_customer["location"],
            money=_customer["money"],
            product_cart=_customer["product_cart"],
            car=_car
        ))

    for _shop in data_dict["shops"]:
        shops.append(Shop(
            name=_shop["name"],
            location=_shop["location"],
            products=_shop["products"]
        ))

    return customers, shops


def shop_trip() -> None:
    customers, shops = init_all_inst()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_cost_dict = {}
        min_cost = 99999
        for shop in shops:
            road_cost = customer.calculate_road_cost(shop, FUEL_PRICE)
            products_cost = customer.calculate_product_cost(shop.products)
            total_cost = products_cost["total"] + road_cost
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost}")

            if total_cost < min_cost and total_cost <= customer.money:
                min_cost_dict["name"] = shop.name
                min_cost_dict["products_cost"] = products_cost
                min_cost_dict["total_cost"] = total_cost
                min_cost = total_cost

        if min_cost == 99999:
            print(f"{customer.name} doesn't have enough money to make "
                  f"purchase in any shop")
            continue

        cur_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{customer.name} rides to {min_cost_dict['name']}\n")
        print(f"Date: {cur_time}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        products_cost = min_cost_dict["products_cost"]
        for product, count in customer.product_cart.items():
            if product in products_cost:
                print(
                    f"{count} {product}s for {products_cost[product]} dollars")
        print(f"Total cost is {products_cost['total']} dollars\n"
              f"See you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{customer.money - min_cost_dict['total_cost']} dollars\n")


if __name__ == "__main__":
    shop_trip()
