import json
from app.customer import make_customer_list
from app.shop import (
    make_shop_list,
    calculate_trip_to_the_shop,
    make_purchase,
    go_to_home
)


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)
        customers = make_customer_list(config)
        shops = make_shop_list(config)
        fuel_price = config["FUEL_PRICE"]

        for customer in customers:
            cheapest_shop = calculate_trip_to_the_shop(
                customer, shops, fuel_price
            )
            if cheapest_shop:
                make_purchase(customer, cheapest_shop)
                go_to_home(customer)


shop_trip()
