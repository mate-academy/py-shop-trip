import json
from app.trip import Trip
from app.person import Person


def shop_trip() -> None:
    with open("app/config.json", "r") as file:

        load = json.load(file)

        fuel_price, customers, shops = load.values()

        for customer in customers:
            person = Person(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]["fuel_consumption"]
            )

            stores = {}

            for shop in shops:
                store = Trip(
                    shop["name"],
                    shop["location"],
                    shop["products"],
                    fuel_price,
                    person.fuel_consumption,
                    person.location
                )

                products = store.money_for_products(person.product_cart)
                trip = store.money_for_trip()
                stores[(sum(products.values()) + trip)] = store

            cheapest_store = stores[min(stores.keys())]
            cheapest_trip = sorted(stores)[0]

            if person.trip(stores, cheapest_store) == "stop":
                break
            person.check(cheapest_store, cheapest_trip)
            person.home()
