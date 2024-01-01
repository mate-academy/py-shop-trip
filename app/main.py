import os
import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_person(config_path: str, entity_type: str) -> list:
    with open(config_path, "r") as file:
        config_data = json.load(file)

    entities = []
    for entity_data in config_data.get(entity_type, []):
        entity = None
        if entity_type == "customers":
            entity = Customer(
                entity_data.get("name", ""),
                entity_data.get("product_cart", {}),
                entity_data.get("location", []),
                entity_data.get("money", 0),
                entity_data.get("car", {})
            )
        elif entity_type == "shops":
            entity = Shop(
                entity_data.get("name", ""),
                entity_data.get("location", []),
                entity_data.get("products", {})
            )
        entities.append(entity)
    return entities


def shop_trip() -> None:
    config_path = os.path.join("app", "config.json")

    with open(config_path, "r") as file:
        config_data = json.load(file)
    fuel_price = config_data.get("FUEL_PRICE", 2.4)

    # Load customers and shops directly in main
    customers = load_person(config_path, "customers")
    shops = load_person(config_path, "shops")

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
            customer.customer_choice(min_trip_cost, cheapest_shop.name)
            if min_trip_cost <= customer.money:
                print()
                print(f"Date: {cheapest_shop.get_current_datetime()}")
                print(f"Thanks, {customer.name}, for your purchase!")

        if min_trip_cost <= customer.money:
            cheapest_shop.products_to_buy(customer, min_trip_cost)


if __name__ == "__main__":
    shop_trip()
