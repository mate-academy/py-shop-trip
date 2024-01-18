import datetime
from decimal import Decimal
from .customer import Customer
from .shop import Shop
from .data_base import DataBase


def format_price(num: int | float) -> int | float:
    if float(num).is_integer():
        return int(num)

    return num


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

        for shop in shops:
            shop_price = (
                (((shop.get_distance(customer.location) / 100) * customer.car[
                    "fuel_consumption"]) * fuel_price) * 2 +
                + shop.products_cost(customer.product_cart)
            )
            shop_price = Decimal(shop_price).quantize(Decimal("0.00"))
            trip_cost[shop_price] = shop
            print(
                f"{customer.name}'s trip to "
                f"the {shop.name} costs {shop_price}"
            )

        money_need = min(trip_cost)

        if money_need > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            break

        money_need = min(trip_cost)
        shop_need = trip_cost[money_need]

        print(f"{customer.name} rides to {shop_need.name}\n")
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )

        print(
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"
        )

        money_spent = 0

        for product, quantity in customer.product_cart.items():
            product_cost = (
                customer.product_cart[product] * shop_need.products[product]
            )
            money_spent += product_cost
            product_quantity = quantity

            print(
                f"{product_quantity} {product}s "
                f"for {format_price(product_cost)} dollars"
            )
        money_left = customer.money - money_need

        print(
            f"Total cost is {money_spent} dollars\n"
            f"See you again!\n"
            f"\n"
            f"{customer.name} rides home\n"
            f"{customer.name} now has {money_left} dollars\n"
        )
