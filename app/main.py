import datetime
from .customer import Customer
from .shop import Shop
from .data_base import DataBase


def shop_trip() -> None:
    data = DataBase()
    customers = []
    shops = []
    fuel_price = data.get_fuel_price()
    trip_cost = {}
    for customer_data in data.get_customers():
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            customer_data["car"]
        )

        customers.append(customer)

    for shop_data in data.get_shops():
        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        for _shop in shops:
            ship_price = round(
                (((_shop.get_distance(customer.location) / 100) * customer.car[
                    "fuel_consumption"]) * fuel_price) * 2 +
                + _shop.products_cost(customer.product_cart), 2
            )
            trip_cost[ship_price] = _shop
            print(
                f"{customer.name}'s trip to "
                f"the {_shop.name} costs {ship_price}"
            )

        money_need = min(trip_cost)

        if money_need > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

        else:
            money_need = min(trip_cost)
            shop_need = trip_cost[money_need]

            print(f"{customer.name} rides to {shop_need.name}\n")
            print(
                f"Date: "
                f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            )
            milk_quantity = customer.product_cart["milk"]
            milk_cost = (
                customer.product_cart["milk"] * shop_need.products["milk"]
            )
            bread_quantity = customer.product_cart["bread"]
            bread_cost = (
                customer.product_cart["bread"] * shop_need.products["bread"]
            )
            butter_quantity = customer.product_cart["butter"]
            butter_cost = (
                customer.product_cart["butter"] * shop_need.products["butter"]
            )

            print(
                f"Thanks, {customer.name}, for your purchase!\n"
                f"You have bought:\n"
                f"{milk_quantity} milks for {milk_cost} dollars\n"
                f"{bread_quantity} breads for {bread_cost} dollars\n"
                f"{butter_quantity} butters for {butter_cost} dollars\n"
                f"Total cost is "
                f"{shop_need.products_cost(customer.product_cart)} dollars\n"
                f"See you again!\n"
            )

            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now "
                f"has {customer.money - money_need} dollars\n"
            )
