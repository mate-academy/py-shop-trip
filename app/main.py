import json
from app.customer import Customer
from app.shop import Shop
from app.calculations import calculate_total_price, purchases_info


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"],
        )
        for customer in data["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_prices = {}
        for shop in shops:
            trip_price = calculate_total_price(customer, shop)
            print(
                f"{customer.name}'s trip"
                f" to the {shop.name} costs {round(trip_price, 2)}"
            )
            trip_prices[trip_price] = shop

        cheapest_trip = min(trip_prices.keys())
        cheapest_shop = trip_prices[cheapest_trip]

        if customer.have_enough_money_to_perform_purchase(cheapest_trip):
            purchases_info(customer, cheapest_shop)
            customer.money -= cheapest_trip
            print(
                f"{customer.name} now has"
                f" {round(customer.money, 2)} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
