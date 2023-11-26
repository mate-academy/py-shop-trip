import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config.get("FUEL_PRICE")
    customers = create_customers_objects(config.get("customers"))
    shops = create_shop_objects(config.get("shops"))
    show_trip(fuel_price, customers, shops)


def create_customers_objects(customers: dict) -> list[Customer]:
    customers_objects = []
    for customer in customers:
        customers_objects.append(Customer(
            customer.get("name"),
            customer.get("product_cart"),
            customer.get("location"),
            customer.get("money"),
            Car(
                customer["car"].get("brand"),
                customer["car"].get("fuel_consumption")
            )
        ))
    return customers_objects


def create_shop_objects(shops: dict) -> list[Shop]:
    shops_objects = []
    for shop in shops:
        shops_objects.append(Shop(
            shop.get("name"),
            shop.get("location"),
            shop.get("products")
        ))
    return shops_objects


def show_trip(
    fuel_price: float,
    customers: list[Customer],
    shops: list[Shop]
) -> None:
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
