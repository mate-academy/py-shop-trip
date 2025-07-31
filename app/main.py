import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = Customer.from_dict(data["customers"])
    shops = Shop.from_dict(data["shops"])

    for customer in customers:
        current_shop, cheapest_shop_price = (
            customer.calculate_cheapest_trip(shops, fuel_price))

        try_trip = customer.make_trip_to_shop(current_shop,
                                              cheapest_shop_price)
        if try_trip:
            current_shop.print_receipt(customer)
            customer.ride_home()
