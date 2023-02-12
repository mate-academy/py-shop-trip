import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file_open:
        data = json.load(file_open)

    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        car = Car(customer.car)

        print(f"{customer.name} has {customer.money} dollars")

        best_option_shop = {}
        for shop in shops:
            distance = customer.get_distance(shop)
            cost = car.cost_of_travel(distance, data["FUEL_PRICE"])
            total_cost = round((shop.calculate_products_price(
                customer.product_cart) + cost), 2)

            if total_cost <= customer.money:
                best_option_shop[total_cost] = shop

            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost}")

        if not best_option_shop:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
            break

        minimal_cost = min(key for key in best_option_shop.keys())

        print(f"{customer.name} rides to "
              f"{best_option_shop[minimal_cost].name}\n")

        best_option_shop[minimal_cost].get_receipt(
            customer.name,
            customer.product_cart
        )
        print(f"{customer.name} rides home")
        print(f"{customer.name} now "
              f"has {customer.money - minimal_cost} dollars\n")
