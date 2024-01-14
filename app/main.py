import json

from app.customer_class import Customer
from app.shop_class import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        fuel_price = data.get("FUEL_PRICE")
        customers = [
            Customer(*customer.values())
            for customer in data.get("customers")
        ]
        shops = [Shop(*shop.values()) for shop in data.get("shops")]
        for customer in customers:
            customer.start_balance()
            dict_with_cost_trip = customer.get_trip_cost(fuel_price, shops)
            cheapest_shop = customer.select_cheapest_trip(dict_with_cost_trip)
            if cheapest_shop is not None:
                cheapest_shop.print_receipt(customer)
                customer.ride_home_and_calculated_money()


shop_trip()
