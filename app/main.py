"""
This module simulates a shopping trip for customers to various shops.

Functions:
    shop_trip() -> None:
        Main function to simulate the shopping trip. It reads configuration
        data, processes customer data, and determines the best shop for each
        customer.

Helper Functions:
    shops_data(data: dict) -> list[Shop]:
        Converts shop data from the configuration into a list of Shop objects.

    customers_data(data: dict) -> list[Customer]:
        Converts customer data from the configuration into a list of Customer
        objects.

    process_customer_data() -> None:
        Processes each customer's data, prints their current money, and
        determines the best shop for them to visit based on fuel price and
        shop data.

Usage:
    Run this module as a script to simulate the shopping trip.
"""
from processing.read_json import open_json_file
from processing.shop import Shop
from processing.customer import Customer


def shop_trip() -> None:

    data = open_json_file("app/config.json")
    fuel_price = data["FUEL_PRICE"]

    def shops_data(data: dict) -> list[Shop]:
        return [Shop(shop) for shop in data.get("shops")]

    def customers_data(data: dict) -> list[Customer]:
        return [Customer(customer) for customer in data.get("customers")]

    def process_shopping_data() -> None:
        for customer in customers_data(data):
            print(f"{customer.name} has {customer.money} dollars")
            cheapest_shop = customer.get_cheapest_shop(
                fuel_price,
                shops_data(data))
            if cheapest_shop:
                customer.ride_to_shop(fuel_price, cheapest_shop)
            else:
                print(
                    f"{customer.name} doesn't have enough money"
                    f" to make a purchase in any shop"
                )

    process_shopping_data()


if __name__ == "__main__":
    shop_trip()
