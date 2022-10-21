import json

from app.initial import to_init


def shop_trip():
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price, list_of_customers, list_of_shops = to_init(data)

    for customer in list_of_customers:
        customer.get_money_before_trip()
        cost_finally = float("inf")
        shop_cheap = None
        for shop in list_of_shops:
            cost = customer.get_full_cost_to_shop(
                shop,
                shop.location,
                fuel_price
            )
            if cost < cost_finally:
                cost_finally = cost
                shop_cheap = shop
        if cost_finally <= customer.money:
            print(f"{customer.name} rides to {shop_cheap.name}\n")
            shop_cheap.get_cheque(customer)
            print(customer.get_money_after_trip(
                shop_cheap.location,
                fuel_price, shop_cheap),
                end="\n\n"
            )
        elif cost_finally > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
