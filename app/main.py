import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> str:
    with open("../config.json", "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops = [Shop(**shop) for shop in config["shops"]]

    for cust in config["customers"]:
        car = Car(**cust["car"])
        customer = Customer(
            name=cust["name"],
            cart=cust["product_cart"],
            location=cust["location"],
            money=cust["money"],
            car=car
        )

        print(f"{customer.name} has {customer.money} dollars")

        trip_cost = []
        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)
            trip_cost.append((cost, shop))
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {cost:.2f}"
            )

        best_cost, best_shop = min(trip_cost, key=lambda x: x[0])

        if not customer.can_afford(best_cost):
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        customer.go_to(best_shop)
        products_cost = best_shop.calculate_cart_cost(customer.cart)
        best_shop.print_receipt(customer, customer.cart, products_cost)
        customer.go_home()

        customer.money -= best_cost
        print(f"{customer.name} now has {customer.money:.2f} dollars\n")
