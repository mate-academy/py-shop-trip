from app.car import Car
from app.customer import Customer
from app.shop import Shop
import json


def shop_trip() -> None:
    with open("app/config.json") as file:
    # with open("config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    customers = [
        Customer(name=customer["name"],
                 product_cart=customer["product_cart"],
                 customer_location=customer["location"],
                 money=customer["money"],
                 car=Car(**customer["car"]))
        for customer in config["customers"]]

    shops = [Shop(name=shop["name"],
                  shop_location=shop["location"],
                  products=shop["products"])
             for shop in config["shops"]]
    for customer in customers:
        cheapest_cost = None
        cheapest_shop = None
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:

            trip_cost = round(customer.calculate_road(shop, fuel_price) * 2 +
                              customer.products_cost(customer.product_cart), 2)

            print(f"{customer.name}\'s trip to the {shop.name} costs {trip_cost}")

            if cheapest_cost is None or trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.shop_location
            customer.money -= cheapest_cost

            customer.print_the_purchase_receipt(cheapest_shop)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
