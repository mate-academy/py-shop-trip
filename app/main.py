import json

from app.car import Car
from app.customers import Customer
from app.shop import Shop


def get_data() -> dict:
    with open("app/config.json", "r") as data_file:
        data = json.load(data_file)
    return data


def create_customer(customer: dict) -> Customer:
    return Customer(
        name=customer.get("name"),
        product_cart=customer.get("product_cart"),
        location=customer.get("location"),
        money=customer.get("money"),
        car=Car(customer.get("car").get("brand"),
                customer.get("car").get("fuel_consumption"),
                fuel_price=get_data().get("FUEL_PRICE"))
    )


def create_shop(shop: dict) -> Shop:
    return Shop(
        name=shop.get("name"),
        location=shop.get("location"),
        products=shop.get("products")
    )


def shop_trip() -> None:
    for customer_data in get_data().get("customers"):
        customer = create_customer(customer_data)
        customer.print_customers_money()

        cost_list = {}
        product_cost = {}
        for shop_data in get_data().get("shops"):
            shop = create_shop(shop_data)
            trip_cost = (shop.distance_cost(customer, customer.car)
                         + shop.product_costs(customer))
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            cost_list[shop.name] = trip_cost
            product_cost[shop.name] = shop.product_costs(customer)

        min_trip_cost = min(cost_list.values())
        cheap_shop = min(cost_list, key=cost_list.get)

        if customer.money < min_trip_cost:
            print(f"{customer.name} doesn't have enough money to make purchase"
                  f" in any shop")
        else:
            print(
                f"{customer.name} rides to {cheap_shop}\n"
                "\nDate: 04/01/2021 12:33:41\n"
                f"Thanks, {customer.name}, for you purchase!\n"
                "You have bought: "
            )

            for shop_data in get_data()["shops"]:
                shop = create_shop(shop_data)
                if shop.name == cheap_shop:
                    shop.print_purchase(customer)

            print(
                f"Total cost is {product_cost[cheap_shop]} dollars\n"
                "See you again!\n"
                f"\n{customer.name} rides home\n"
                f"{customer.name} now has {customer.money - min_trip_cost} "
                f"dollars\n"
            )
