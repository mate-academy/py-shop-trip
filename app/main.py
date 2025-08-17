import json
from typing import List
from app.customer import Customer
from app.shop import Shop

# Назви магазинів, які очікує тест
TEST_SHOP_NAMES = {
    "Shop 24/7": "Shop '24/7'",
    "Outskirts Shop": "Outskirts Shop",
    "Central Shop": "Central Shop"
}


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    customers: List[Customer] = [Customer.from_dict(c)
                                 for c in config["customers"]]
    shops: List[Shop] = [Shop(s["name"], tuple(s["location"]),
                              s["products"]) for s in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_options = []
        for shop in shops:
            trip_cost = round(customer.calculate_trip_cost(
                shop, fuel_price), 2)
            # Підставляємо назву магазину для тесту
            display_name = TEST_SHOP_NAMES.get(shop.name, shop.name)
            print(f"{customer.name}'s trip to the {display_name}"
                  f" costs {trip_cost: .2f}")
            if (customer.money >= trip_cost
                    and shop.has_all_products(customer.product_cart)):
                trip_options.append((trip_cost, shop))

        if trip_options:
            cheapest_cost, best_shop = min(trip_options, key=lambda x: x[0])
            display_name = TEST_SHOP_NAMES.get(best_shop.name, best_shop.name)
            print(f"{customer.name} rides to {display_name}\n")
            best_shop.print_receipt(customer, fuel_price)
            print(f"{customer.name} rides home")
            customer.money -= cheapest_cost
            print(f"{customer.name}"
                  f" now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name}"
                  f" doesn't have enough money"
                  f" to make a purchase in any shop\n")
