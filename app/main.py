import os
import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_entities(config_path: str) -> tuple:
    with open(config_path, "r") as file:
        config_data = json.load(file)

    customers = []
    for customer_data in config_data.get("customers", []):
        customer = Customer(**customer_data)
        customers.append(customer)

    shops = []
    for shop_data in config_data.get("shops", []):
        shop = Shop(**shop_data)
        shops.append(shop)

    fuel_price = config_data.get("FUEL_PRICE", 2.4)

    return customers, shops, fuel_price


def shop_trip() -> None:
    config_path = os.path.join("app", "config.json")

    customers, shops, fuel_price = load_entities(config_path)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_trip_cost = float("inf")
        cheapest_shop = None

        for shop in shops:
            trip_cost = Car(
                customer.car["brand"],
                customer.car["fuel_consumption"],
                fuel_price,
                customer.product_cart
            ).shop_expenses(shop, customer.location)

            print(
                f"{customer.name}'s trip to "
                f"the {shop.name} costs {trip_cost}"
            )

            if trip_cost < min_trip_cost:
                min_trip_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            customer.location = cheapest_shop.location
            customer.customer_choice(min_trip_cost, cheapest_shop.name)
            if min_trip_cost <= customer.money:
                print(f"\nDate: {cheapest_shop.get_current_datetime()}\n"
                      f"Thanks, {customer.name}, for your purchase!")

        if min_trip_cost <= customer.money:
            cheapest_shop.products_to_buy(customer, min_trip_cost)


if __name__ == "__main__":
    shop_trip()
