import json

from app.trip.customer import Customer
from app.shopping_implementation.shop import Shop


def shop_trip() -> None:
    with open("C:\\Users\\user\\Desktop\\mate_tasks"
              "\\py-shop-trip\\app\\config.json") as config:
        inf_total = json.load(config)
    fuel_price = inf_total.get("FUEL_PRICE")
    customers = [
        Customer.from_dict(customer, fuel_price)
        for customer in inf_total.get("customers")
    ]
    shops = [Shop.from_dict(shop) for shop in inf_total.get("shops")]
    for customer in customers:
        customer.count_money()
        for shop in shops:
            customer.calculate_trip_cost(shop)
        chosen_shop = customer.decision()
        if chosen_shop:
            chosen_shop.give_receipt(customer)
            customer.go_home()
            customer.count_money(True)
