import json

from app.customer import Customer
from app.logic_funcs import counting_product_price, counting_trips
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as source:
        info = json.load(source)

    customers = [Customer(**customer) for customer in info["customers"]]
    shops = {market["name"]: Shop(**market) for market in info["shops"]}

    for person in customers:
        counted_trip = counting_trips(person, shops, info["FUEL_PRICE"])
        best_trip = min(counted_trip)
        if best_trip > person.money:
            print(
                f"{person} doesn't have enough money "
                f"to make purchase in any shop"
            )
        else:
            cheapest_shop = counted_trip[best_trip]
            person.ride_to_shop(cheapest_shop)
            counting_product_price(person, shops, cheapest_shop)
            person.ride_to_home(price=best_trip)


if __name__ == "__main__":
    shop_trip()
