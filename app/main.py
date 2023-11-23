import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config.get("FUEL_PRICE")
    customers = []
    for el in config.get("customers"):
        customers.append(Customer(
            el.get("name"),
            el.get("product_cart"),
            el.get("location"),
            el.get("money"),
            Car(
                el.get("car").get("brand"),
                el.get("car").get("fuel_consumption")
            )
        ))

    shops = []
    for el in config.get("shops"):
        shops.append(Shop(
            el.get("name"),
            el.get("location"),
            el.get("products")
        ))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = customer.choose_shop(shops, fuel_price)
        if cheapest_shop.get("total_cost") > customer.money:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
        else:
            cheapest_shop_name = cheapest_shop.get("shop").name
            print(f"{customer.name} rides to {cheapest_shop_name}\n")
            receipt, total_cost = cheapest_shop["shop"].get_receipt(
                customer.to_buy,
                customer.name
            )
            print(receipt)
            print(f"{customer.name} rides home")
            customer_money = round(
                customer.money - cheapest_shop.get("total_cost"),
                2
            )
            print(
                f"{customer.name} now has "
                f"{customer_money} dollars\n"
            )
