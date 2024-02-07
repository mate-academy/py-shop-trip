import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_info = json.load(file)
        Customer.create_from_dict(json_info["customers"])
        Shop.create_from_dict(json_info["shops"])

    for customer in Customer.customer_list:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_trip = customer.money
        shop_to_go = None

        for shop in Shop.shop_list:
            cost_of_the_trip = customer.cost_of_the_trip(shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost_of_the_trip}")
            if not shop_to_go or cost_of_the_trip < cheapest_trip:
                shop_to_go = shop
                cheapest_trip = cost_of_the_trip

        if cheapest_trip >= customer.money:
            print(f"{customer.name} doesn't have enough money"
                  f" to make purchase in any shop")
        else:
            customer.shopping(shop_to_go, cheapest_trip)
